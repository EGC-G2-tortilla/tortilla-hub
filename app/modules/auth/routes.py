import os
import secrets
import string
from dotenv import load_dotenv
from flask import render_template, redirect, url_for, session, request, Flask
from flask_login import current_user, login_user, logout_user
from werkzeug.security import generate_password_hash

from authlib.integrations.flask_client import OAuth

from app.modules.auth import auth_bp
from app.modules.auth.forms import ProvideEmailForm, SignupForm, LoginForm
from app.modules.auth.services import AuthenticationService
from app.modules.profile.services import UserProfileService

load_dotenv()
authentication_service = AuthenticationService()
user_profile_service = UserProfileService()

app = Flask(__name__)
app.secret_key = 'random secret key'

# OAuth configuration
oauth = OAuth(app)
google = oauth.register(
    name='google',
    client_id=os.getenv('GOOGLE_CLIENT_ID'),
    client_secret=os.getenv('GOOGLE_CLIENT_SECRET'),
    server_metadata_url='https://accounts.google.com/.well-known/openid-configuration',
    client_kwargs={'scope': 'openid profile email'})

github = oauth.register(
    name='github',
    client_id=os.getenv('GITHUB_CLIENT_ID'),
    client_secret=os.getenv('GITHUB_CLIENT_SECRET'),
    access_token_url='https://github.com/login/oauth/access_token',
    access_token_params=None,
    authorize_url='https://github.com/login/oauth/authorize',
    authorize_params=None,
    api_base_url='https://api.github.com/',
    client_kwargs={'scope': 'user:email read:user'},
    )

orcid = oauth.register(
    name='orcid',
    client_id=os.getenv('ORCID_CLIENT_ID'),
    client_secret=os.getenv('ORCID_CLIENT_SECRET'),
    authorize_url='https://orcid.org/oauth/authorize',
    access_token_url='https://orcid.org/oauth/token',
    client_kwargs={'scope': '/authenticate', 'token_endpoint_auth_method': 'client_secret_post'}
)


def generate_random_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(secrets.choice(characters) for i in range(length))


@auth_bp.route("/signup/", methods=["GET", "POST"])
def show_signup_form():
    if current_user.is_authenticated:
        return redirect(url_for('public.index'))

    # Genera un estado único para la sesión
    state = secrets.token_urlsafe(16)
    session['signup_state'] = state

    form = SignupForm()
    if form.validate_on_submit():
        email = form.email.data
        if not authentication_service.is_email_available(email):
            message = f'Email {email} in use'
            if authentication_service.get_by_email(email).is_oauth_user():
                message += ' by another provider (OAuth)'
            return render_template("auth/signup_form.html", form=form, error=message)

        try:
            user = authentication_service.create_with_profile(**form.data)
        except Exception as exc:
            return render_template("auth/signup_form.html", form=form, error=f'Error creating user: {exc}')

        # Log user
        login_user(user, remember=True)
        return redirect(url_for('public.index'))

    return render_template("auth/signup_form.html", form=form, state=state)


@auth_bp.route("/signup/orcid")
def sign_up_orcid():
    # Genera un estado único para la sesión y almacénalo
    state = secrets.token_urlsafe(16)
    session['signup_state'] = state

    # Redirige a ORCID con el estado generado
    redirect_uri = url_for("auth.authorize_signup_orcid", _external=True)
    return orcid.authorize_redirect(redirect_uri, state=state)


@auth_bp.route("/authorize/signup/orcid")
def authorize_signup_orcid():
    if current_user.is_authenticated:
        return redirect(url_for('public.index'))

    # Verifica que el estado almacenado en la sesión coincida con el estado recibido
    state = request.args.get('state')
    expected_state = session.pop('signup_state', None)
    if state != expected_state:
        return "CSRF Warning! State mismatch.", 400

    # Autoriza el token con ORCID
    token = orcid.authorize_access_token()
    orcid_id = token.get('orcid')

    # Solicitar la información del perfil del usuario
    userinfo_endpoint = f"https://pub.orcid.org/v3.0/{orcid_id}"
    headers = {'Accept': 'application/json'}
    resp = orcid.get(userinfo_endpoint, headers=headers)
    profile = resp.json()

    # Obtener email adicionalmente desde el endpoint de emails de ORCID
    email_endpoint = f"https://pub.orcid.org/v3.0/{orcid_id}/email"
    email_resp = orcid.get(email_endpoint, headers=headers)
    email_data = email_resp.json()
    email = next(
        (email['email'] for email in email_data.get('email', [])
         if email.get('primary') and email.get('verified')),
        None
    )
    if not email:
        # Si el email no está disponible, redirige al usuario a una página donde pueda proporcionarlo manualmente
        session['orcid_id'] = orcid_id
        session['profile_data'] = {
            'given_name': profile.get("person", {}).get("name", {}).get("given-names", {}).get("value", "No Name"),
            'family_name': profile.get("person", {}).get("name", {}).get("family-name", {}).get("value", "No Surname"),
        }
        return redirect(url_for('auth.provide_email'))

    given_name = profile.get("person", {}).get("name", {}).get("given-names", {}).get("value", "No Name")
    family_name = profile.get("person", {}).get("name", {}).get("family-name", {}).get("value", "No Surname")

    user = authentication_service.get_by_email(email)

    if user and user.is_oauth_user():
        login_user(user, remember=True)
        return redirect(url_for('public.index'))

    elif user:
        form = SignupForm()
        return render_template("auth/signup_form.html", form=form, error="Email already in use, try logging in")

    random_password = generate_random_password()
    hashed_password = generate_password_hash(random_password)

    user = authentication_service.create_with_profile_and_oauth_provider_appended(
        email=email,
        password=hashed_password,
        name=given_name,
        surname=family_name,
        oauth_provider='orcid',
        oauth_provider_user_id=orcid_id,
        orcid=orcid_id
    )
    login_user(user, remember=True)
    return redirect(url_for('public.index'))


@auth_bp.route("/provide_email", methods=["GET", "POST"])
def provide_email():
    form = ProvideEmailForm()
    if request.method == "POST" and form.validate_on_submit():
        email = form.email.data
        # Recupera los datos almacenados en la sesión
        orcid_id = session.pop('orcid_id', None)
        profile_data = session.pop('profile_data', {})

        given_name = profile_data.get('given_name', "No Name")
        family_name = profile_data.get('family_name', "No Surname")

        user = authentication_service.get_by_email(email)

        if user and user.is_oauth_user():
            login_user(user, remember=True)
            return redirect(url_for('public.index'))

        elif user:
            return render_template("auth/provide_email.html", form=form, error="Email already in use, try logging in")

        random_password = generate_random_password()
        hashed_password = generate_password_hash(random_password)

        user = authentication_service.create_with_profile_and_oauth_provider_appended(
            email=email,
            password=hashed_password,
            name=given_name,
            surname=family_name,
            oauth_provider='orcid',
            oauth_provider_user_id=orcid_id,
            orcid=orcid_id
        )
        login_user(user, remember=True)
        return redirect(url_for('public.index'))

    return render_template("auth/provide_email.html", form=form)


@auth_bp.route("/login/orcid")
def login_orcid():
    # Genera un estado único para la sesión y almacénalo
    state = secrets.token_urlsafe(16)
    session['login_state'] = state

    # Redirige a ORCID con el estado generado
    redirect_uri = url_for("auth.authorize_login_orcid", _external=True)
    return orcid.authorize_redirect(redirect_uri, state=state)


@auth_bp.route("/authorize/login/orcid")
def authorize_login_orcid():
    if current_user.is_authenticated:
        return redirect(url_for('public.index'))

    # Verifica que el estado almacenado en la sesión coincida con el estado recibido
    state = request.args.get('state')
    expected_state = session.pop('login_state', None)
    if state != expected_state:
        return "CSRF Warning! State mismatch.", 400

    # Autoriza el token con ORCID
    token = orcid.authorize_access_token()
    orcid_id = token.get('orcid')

    # Buscar al usuario en la base de datos utilizando el ORCID ID
    user = authentication_service.get_by_orcid(orcid_id)

    # Si el usuario existe, proceder con el login
    if user:
        login_user(user, remember=True)
        return redirect(url_for('public.index'))

    # Si el usuario no existe, devolver un mensaje de error
    form = LoginForm()
    return render_template("auth/login_form.html", form=form, error="Account with this ORCID ID does not exist")


@auth_bp.route("/signup/google")
def sign_up_google():
    if session.get('signup_state') is None:
        return redirect(url_for('auth.show_signup_form'))
    redirect_uri = url_for('auth.authorize_signup_google', _external=True)
    return google.authorize_redirect(redirect_uri)


@auth_bp.route("/signup/github")
def sign_up_github():
    if session.get('signup_state') is None:
        return redirect(url_for('auth.show_signup_form'))
    redirect_uri = url_for('auth.authorize_github', _external=True, flow='signup')
    return github.authorize_redirect(redirect_uri)


@auth_bp.route("/authorize/signup/google")
def authorize_signup_google():
    if current_user.is_authenticated and session.get('signup_state') is None:
        return redirect(url_for('public.index'))
    if not current_user.is_authenticated and session.get('signup_state') is None:
        return redirect(url_for('auth.show_signup_form'))
    google.authorize_access_token()
    userinfo_endpoint = google.server_metadata['userinfo_endpoint']
    resp = google.get(userinfo_endpoint)
    profile = resp.json()
    user = authentication_service.get_by_email(profile['email'])

    # Comprueba si el usuario ya existe en la base de datos y si es un usuario de OAuth
    if user and user.is_oauth_user():
        login_user(user, remember=True)
        session.pop('signup_state')  # Eliminar estado de signup
        return redirect(url_for('public.index'))

    # Si el usuario ya existe en la base de datos pero no es un usuario de OAuth
    elif user:
        form = SignupForm()
        return render_template("auth/signup_form.html", form=form, error="Email already in use, try logging in")

    # Si el usuario no existe en la base de datos
    else:
        random_password = generate_random_password()

        # Crear una variable con una contraseña hash
        hashed_password = generate_password_hash(random_password)
        # Crear un usuario con el email y la contraseña hash
        surname = profile.get('family_name', 'No Surname')
        user = authentication_service.create_with_profile_and_oauth_provider_appended(
            email=profile['email'],
            password=hashed_password,
            name=profile['given_name'],
            surname=surname,
            oauth_provider='google',
            oauth_provider_user_id=profile['sub']
        )
        # Log user
        login_user(user, remember=True)
        session.pop('signup_state')  # Eliminar estado de signup
        return redirect(url_for('public.index'))


@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('public.index'))

    # Genera un estado único para la sesión
    state = secrets.token_urlsafe(16)
    session['login_state'] = state

    form = LoginForm()
    if request.method == 'POST' and form.validate_on_submit():
        if authentication_service.login(form.email.data, form.password.data):
            return redirect(url_for('public.index'))

        return render_template("auth/login_form.html", form=form, error='Invalid credentials')

    return render_template('auth/login_form.html', form=form, state=state)


@auth_bp.route('/login/google')
def login_google():
    redirect_uri = url_for('auth.authorize_login_google', _external=True)
    return google.authorize_redirect(redirect_uri)


@auth_bp.route('/login/github')
def login_github():
    redirect_uri = url_for('auth.authorize_github', _external=True, flow='login')
    return github.authorize_redirect(redirect_uri)


@auth_bp.route("/authorize/login/google")
def authorize_login_google():
    if current_user.is_authenticated and session.get('login_state') is None:
        return redirect(url_for('public.index'))
    if not current_user.is_authenticated and session.get('login_state') is None:
        return redirect(url_for('auth.login'))
    google.authorize_access_token()
    userinfo_endpoint = google.server_metadata['userinfo_endpoint']
    resp = google.get(userinfo_endpoint)
    profile = resp.json()
    user = authentication_service.get_by_email(profile['email'])

    # Comprueba si el usuario ya existe en la base de datos y si es un usuario de OAuth
    if user and user.is_oauth_user():
        session.pop('login_state')  # Eliminar estado de login
        login_user(user, remember=True)
        return redirect(url_for('public.index'))

    # Si el usuario ya existe en la base de datos pero no es un usuario de OAuth
    elif user:
        form = LoginForm()
        return render_template("auth/login_form.html", form=form, error="Email already in use")

    # Si el usuario no existe en la base de datos
    else:
        random_password = generate_random_password()

        # Crear una variable con una contraseña hash
        hashed_password = generate_password_hash(random_password)
        # Crear un usuario con el email y la contraseña hash
        surname = profile.get('family_name', 'No Surname')
        user = authentication_service.create_with_profile_and_oauth_provider_appended(
            email=profile['email'],
            password=hashed_password,
            name=profile['given_name'],
            surname=surname,
            oauth_provider='google',
            oauth_provider_user_id=profile['sub']
        )
        # Log user
        session.pop('login_state')  # Eliminar estado de login
        login_user(user, remember=True)

        return redirect(url_for('public.index'))


@auth_bp.route("/authorize/github")
def authorize_github():
    if current_user.is_authenticated:
        return redirect(url_for('public.index'))
    flow = request.args.get('flow')
    if (not flow or (flow not in ['signup', 'login']) or
            (flow == 'signup' and session.get('signup_state') is None) or
            (flow == 'login' and session.get('login_state') is None)):
        return redirect(url_for('public.index'))
    github.authorize_access_token()
    resp = github.get('user')
    profile = resp.json()

    # Obtener email si no está en el perfil principal
    if 'email' not in profile or not profile['email']:
        emails_resp = github.get('user/emails')
        profile['email'] = next((email_data['email'] for email_data in emails_resp.json() if email_data.get('primary')
                                 and email_data.get('verified')), None)

    if not profile.get('email'):
        session.pop('signup_state', None)
        session.pop('login_state', None)
        return render_template(
            "auth/show_signup_form.html" if flow == 'signup' else "auth/login_form.html",
            form=SignupForm() if flow == 'signup' else LoginForm(),
            error="Email not available from GitHub")
    user = authentication_service.get_by_email(profile['email'])

    if user:
        if user.is_oauth_user():
            login_user(user, remember=True)
            return redirect(url_for('public.index'))

        session.pop('signup_state', None)
        session.pop('login_state', None)
        return render_template("auth/show_signup_form.html"
                               if flow == 'signup' else "auth/login_form.html", form=SignupForm()
                               if flow == 'signup' else LoginForm(), error="Email already in use")

    # Crear usuario si no existe
    random_password = generate_random_password()
    hashed_password = generate_password_hash(random_password)
    name = profile.get('name', profile.get('login'))
    surname = profile.get('family_name', 'No Surname')
    user = authentication_service.create_with_profile_and_oauth_provider_appended(
        email=profile['email'],
        password=hashed_password,
        name=name,
        surname=surname,
        oauth_provider='github',
        oauth_provider_user_id=profile['id']
    )

    login_user(user, remember=True)
    session.pop('signup_state', None)
    session.pop('login_state', None)
    session.pop('s')
    return redirect(url_for('public.index'))


@auth_bp.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('public.index'))

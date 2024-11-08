import os
import secrets
import string
from dotenv import load_dotenv
from flask import render_template, redirect, url_for, request, Flask
from flask_login import current_user, login_user, logout_user
from werkzeug.security import generate_password_hash

from authlib.integrations.flask_client import OAuth

from app.modules.auth import auth_bp
from app.modules.auth.forms import SignupForm, LoginForm
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


def generate_random_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(secrets.choice(characters) for i in range(length))


@auth_bp.route("/signup/", methods=["GET", "POST"])
def show_signup_form():
    if current_user.is_authenticated:
        return redirect(url_for('public.index'))

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

    return render_template("auth/signup_form.html", form=form)


@auth_bp.route("/signup/google")
def sign_up_google():
    redirect_uri = url_for('auth.authorize_signup_google', _external=True)
    return google.authorize_redirect(redirect_uri)


@auth_bp.route("/authorize/signup/google")
def authorize_signup_google():
    google.authorize_access_token()
    userinfo_endpoint = google.server_metadata['userinfo_endpoint']
    resp = google.get(userinfo_endpoint)
    profile = resp.json()
    user = authentication_service.get_by_email(profile['email'])
    
    # Comprueba si el usuario ya existe en la base de datos y si es un usuario de OAuth
    if user and user.is_oauth_user():
        login_user(user, remember=True)
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

        return redirect(url_for('public.index'))


@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('public.index'))

    form = LoginForm()
    if request.method == 'POST' and form.validate_on_submit():
        if authentication_service.login(form.email.data, form.password.data):
            return redirect(url_for('public.index'))

        return render_template("auth/login_form.html", form=form, error='Invalid credentials')

    return render_template('auth/login_form.html', form=form)


@auth_bp.route('/login/google')
def login_google():
    redirect_uri = url_for('auth.authorize_login_google', _external=True)
    return google.authorize_redirect(redirect_uri)


@auth_bp.route("/authorize/login/google")
def authorize_login_google():
    google.authorize_access_token()
    userinfo_endpoint = google.server_metadata['userinfo_endpoint']
    resp = google.get(userinfo_endpoint)
    profile = resp.json()
    user = authentication_service.get_by_email(profile['email'])
    
    # Comprueba si el usuario ya existe en la base de datos y si es un usuario de OAuth
    if user and user.is_oauth_user():
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
        login_user(user, remember=True)

        return redirect(url_for('public.index'))


@auth_bp.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('public.index'))

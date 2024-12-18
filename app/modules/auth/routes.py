import os
import secrets
import string
from dotenv import load_dotenv
from flask import jsonify, render_template, redirect, url_for, session, request, Flask
from flask_login import current_user, login_user, logout_user
import requests
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
app.secret_key = "random secret key"

# OAuth configuration
oauth = OAuth(app)
google = oauth.register(
    name="google",
    client_id=os.getenv("GOOGLE_CLIENT_ID"),
    client_secret=os.getenv("GOOGLE_CLIENT_SECRET"),
    server_metadata_url="https://accounts.google.com/.well-known/openid-configuration",
    client_kwargs={"scope": "openid profile email"},
)

github = oauth.register(
    name="github",
    client_id=os.getenv("GITHUB_CLIENT_ID"),
    client_secret=os.getenv("GITHUB_CLIENT_SECRET"),
    access_token_url="https://github.com/login/oauth/access_token",
    access_token_params=None,
    authorize_url="https://github.com/login/oauth/authorize",
    authorize_params=None,
    api_base_url="https://api.github.com/",
    client_kwargs={"scope": "repo user:email read:user"},
)

orcid = oauth.register(
    name="orcid",
    client_id=os.getenv("ORCID_CLIENT_ID"),
    client_secret=os.getenv("ORCID_CLIENT_SECRET"),
    authorize_url="https://orcid.org/oauth/authorize",
    access_token_url="https://orcid.org/oauth/token",
    client_kwargs={
        "scope": "/authenticate",
        "token_endpoint_auth_method": "client_secret_post",
    },
)

gitlab = oauth.register(
    name="gitlab",
    client_id=os.getenv("GITLAB_CLIENT_ID"),
    client_secret=os.getenv("GITLAB_CLIENT_SECRET"),
    authorize_url="https://gitlab.com/oauth/authorize",
    access_token_url="https://gitlab.com/oauth/token",
    api_base_url="https://gitlab.com/api/v4/",
    client_kwargs={"scope": "api"},
)


def generate_random_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    return "".join(secrets.choice(characters) for i in range(length))


@auth_bp.route("/signup/", methods=["GET", "POST"])
def show_signup_form():
    if current_user.is_authenticated:
        return redirect(url_for("public.index"))

    # Genera un estado único para la sesión
    state = secrets.token_urlsafe(16)
    session["signup_state"] = state

    form = SignupForm()
    if form.validate_on_submit():
        email = form.email.data
        if not authentication_service.is_email_available(email):
            message = f"Email {email} in use"
            if authentication_service.get_by_email(email).is_oauth_user():
                message += " by another provider (OAuth)"
            return render_template("auth/signup_form.html", form=form, error=message)

        try:
            user = authentication_service.create_with_profile(**form.data)
        except Exception as exc:
            return render_template(
                "auth/signup_form.html", form=form, error=f"Error creating user: {exc}"
            )

        # Log user
        login_user(user, remember=True)
        return redirect(url_for("public.index"))

    return render_template("auth/signup_form.html", form=form, state=state)


@auth_bp.route("/login", methods=["GET", "POST"])
def login():
    if current_user.is_authenticated:
        return redirect(url_for("public.index"))

    # Genera un estado único para la sesión
    state = secrets.token_urlsafe(16)
    session["login_state"] = state

    form = LoginForm()
    if request.method == "POST" and form.validate_on_submit():
        if authentication_service.login(form.email.data, form.password.data):
            return redirect(url_for("public.index"))

        return render_template(
            "auth/login_form.html", form=form, error="Invalid credentials"
        )

    return render_template("auth/login_form.html", form=form, state=state)


@auth_bp.route("/signup/orcid")
def sign_up_orcid():
    # Genera un estado único para la sesión y almacénalo
    state = secrets.token_urlsafe(16)
    session["signup_state"] = state

    # Redirige a ORCID con el estado generado
    redirect_uri = url_for("auth.authorize_signup_orcid", _external=True)
    return orcid.authorize_redirect(redirect_uri, state=state)


@auth_bp.route("/authorize/signup/orcid")
def authorize_signup_orcid():
    if current_user.is_authenticated:
        return redirect(url_for("public.index"))

    # Verifica que el estado almacenado en la sesión coincida con el estado recibido
    state = request.args.get("state")
    expected_state = session.pop("signup_state", None)
    if state != expected_state:
        return "CSRF Warning! State mismatch.", 400

    # Autoriza el token con ORCID
    token = orcid.authorize_access_token()
    orcid_id = token.get("orcid")

    # Solicitar la información del perfil del usuario
    userinfo_endpoint = f"https://pub.orcid.org/v3.0/{orcid_id}"
    headers = {"Accept": "application/json"}
    resp = orcid.get(userinfo_endpoint, headers=headers)
    profile = resp.json()

    # Obtener email adicionalmente desde el endpoint de emails de ORCID
    email_endpoint = f"https://pub.orcid.org/v3.0/{orcid_id}/email"
    email_resp = orcid.get(email_endpoint, headers=headers)
    email_data = email_resp.json()
    email = next(
        (
            email["email"]
            for email in email_data.get("email", [])
            if email.get("primary") and email.get("verified")
        ),
        None,
    )
    if not email:
        # Si el email no está disponible, redirige al usuario a una página donde pueda proporcionarlo manualmente
        session["orcid_id"] = orcid_id
        session["profile_data"] = {
            "given_name": profile.get("person", {})
            .get("name", {})
            .get("given-names", {})
            .get("value", "No Name"),
            "family_name": profile.get("person", {})
            .get("name", {})
            .get("family-name", {})
            .get("value", "No Surname"),
        }
        return redirect(url_for("auth.provide_email"))

    given_name = (
        profile.get("person", {})
        .get("name", {})
        .get("given-names", {})
        .get("value", "No Name")
    )
    family_name = (
        profile.get("person", {})
        .get("name", {})
        .get("family-name", {})
        .get("value", "No Surname")
    )

    user = authentication_service.get_by_email(email)

    if user:
        is_orcid_user = next(
            (
                provider
                for provider in user.oauth_providers
                if provider.provider_name == "orcid"
            ),
            None,
        )
        # Si el usuario ya existe en la base de datos, añadir una nueva conexión ORCID si esta no existe
        if not is_orcid_user:
            authentication_service.append_oauth_provider(user, "orcid", orcid_id)
        login_user(user, remember=True)
        return redirect(url_for("public.index"))

    else:

        random_password = generate_random_password()
        hashed_password = generate_password_hash(random_password)

        user = authentication_service.create_with_profile_and_oauth_provider_appended(
            email=email,
            password=hashed_password,
            name=given_name,
            surname=family_name,
            oauth_provider="orcid",
            oauth_provider_user_id=orcid_id,
            orcid=orcid_id,
        )
        login_user(user, remember=True)
        return redirect(url_for("public.index"))


@auth_bp.route("/provide_email", methods=["GET", "POST"])
def provide_email():
    form = ProvideEmailForm()
    if request.method == "POST" and form.validate_on_submit():
        email = form.email.data
        # Recupera los datos almacenados en la sesión
        orcid_id = session.pop("orcid_id", None)
        profile_data = session.pop("profile_data", {})

        given_name = profile_data.get("given_name", "No Name")
        family_name = profile_data.get("family_name", "No Surname")

        user = authentication_service.get_by_email(email)

        if user:
            is_orcid_user = next(
                (
                    provider
                    for provider in user.oauth_providers
                    if provider.provider_name == "orcid"
                ),
                None,
            )
            # Si el usuario ya existe en la base de datos y es OAuth, añadir una nueva conexión ORCID si esta no existe
            if not is_orcid_user:
                authentication_service.append_oauth_provider(user, "orcid", orcid_id)
            login_user(user, remember=True)
            return redirect(url_for("public.index"))

        else:
            random_password = generate_random_password()
            hashed_password = generate_password_hash(random_password)

            user = (
                authentication_service.create_with_profile_and_oauth_provider_appended(
                    email=email,
                    password=hashed_password,
                    name=given_name,
                    surname=family_name,
                    oauth_provider="orcid",
                    oauth_provider_user_id=orcid_id,
                    orcid=orcid_id,
                )
            )
            login_user(user, remember=True)
            return redirect(url_for("public.index"))

    return render_template("auth/provide_email.html", form=form)


@auth_bp.route("/login/orcid")
def login_orcid():
    # Genera un estado único para la sesión y almacénalo
    state = secrets.token_urlsafe(16)
    session["login_state"] = state

    # Redirige a ORCID con el estado generado
    redirect_uri = url_for("auth.authorize_login_orcid", _external=True)
    return orcid.authorize_redirect(redirect_uri, state=state)


@auth_bp.route("/authorize/login/orcid")
def authorize_login_orcid():
    if current_user.is_authenticated:
        return redirect(url_for("public.index"))

    # Verifica que el estado almacenado en la sesión coincida con el estado recibido
    state = request.args.get("state")
    expected_state = session.pop("login_state", None)
    if state != expected_state:
        return "CSRF Warning! State mismatch.", 400

    # Autoriza el token con ORCID
    token = orcid.authorize_access_token()
    orcid_id = token.get("orcid")

    # Buscar al usuario en la base de datos utilizando el ORCID ID
    user = authentication_service.get_by_orcid(orcid_id)

    # Si el usuario existe, proceder con el login
    if user:
        login_user(user, remember=True)
        return redirect(url_for("public.index"))

    # Si el usuario no existe, devolver un mensaje de error
    form = LoginForm()
    return render_template(
        "auth/login_form.html",
        form=form,
        error="Account with this ORCID ID does not exist",
    )


@auth_bp.route("/signup/google")
def sign_up_google():
    if session.get("signup_state") is None:
        return redirect(url_for("auth.show_signup_form"))
    redirect_uri = url_for("auth.authorize_signup_google", _external=True)
    return google.authorize_redirect(redirect_uri)


@auth_bp.route("/authorize/signup/google")
def authorize_signup_google():
    if current_user.is_authenticated and session.get("signup_state") is None:
        return redirect(url_for("public.index"))
    if not current_user.is_authenticated and session.get("signup_state") is None:
        return redirect(url_for("auth.show_signup_form"))
    google.authorize_access_token()
    userinfo_endpoint = google.server_metadata["userinfo_endpoint"]
    resp = google.get(userinfo_endpoint)
    profile = resp.json()
    user = authentication_service.get_by_email(profile["email"])

    # Comprueba si el usuario ya existe en la base de datos
    if user:
        is_google_user = next(
            # Si el usuario ya existe en la base de datos y es OAuth, añadir una nueva conexión Google si esta no existe
            (
                provider
                for provider in user.oauth_providers
                if provider.provider_name == "google"
            ),
            None,
        )
        # Si el usuario ya existe en la base de datos, añadir una nueva conexión Google si esta no existe
        if not is_google_user:
            authentication_service.append_oauth_provider(user, "google", profile["sub"])
        login_user(user, remember=True)
        session.pop("signup_state")  # Eliminar estado de signup
        return redirect(url_for("public.index"))

    else:
        random_password = generate_random_password()

        # Crear una variable con una contraseña hash
        hashed_password = generate_password_hash(random_password)
        # Crear un usuario con el email y la contraseña hash
        surname = profile.get("family_name", "No Surname")
        user = authentication_service.create_with_profile_and_oauth_provider_appended(
            email=profile["email"],
            password=hashed_password,
            name=profile["given_name"],
            surname=surname,
            oauth_provider="google",
            oauth_provider_user_id=profile["sub"],
        )
        # Log user
        login_user(user, remember=True)
        session.pop("signup_state")  # Eliminar estado de signup
        return redirect(url_for("public.index"))


@auth_bp.route("/login/google")
def login_google():
    redirect_uri = url_for("auth.authorize_login_google", _external=True)
    return google.authorize_redirect(redirect_uri)


@auth_bp.route("/authorize/login/google")
def authorize_login_google():
    if current_user.is_authenticated:
        return redirect(url_for("public.index"))

    # Verifica que el estado almacenado en la sesión coincida con el estado recibido
    if session.get("login_state") is None:
        return redirect(url_for("auth.login"))

    # Autoriza el token y obtiene la información del perfil del usuario
    google.authorize_access_token()
    userinfo_endpoint = google.server_metadata["userinfo_endpoint"]
    resp = google.get(userinfo_endpoint)
    profile = resp.json()

    # Verificar si el usuario ya está registrado
    user = authentication_service.get_by_email(profile["email"])

    if user:
        # Comprobar si el usuario tiene Google como proveedor OAuth
        is_google_user = next(
            (
                provider
                for provider in user.oauth_providers
                if provider.provider_name == "google"
            ),
            None,
        )

        # Si el usuario ya existe pero no tiene Google vinculado, añadimos la conexión
        if not is_google_user:
            authentication_service.append_oauth_provider(user, "google", profile["sub"])

        # Loguear al usuario
        session.pop("login_state", None)
        session.pop("signup_state", None)
        login_user(user, remember=True)
        return redirect(url_for("public.index"))

    else:
        # Si el usuario no existe, redirigir al login con un mensaje de error
        session.pop("login_state", None)
        return redirect(
            url_for("auth.login")
            + "?error=This account does not exist. Please sign up."
        )


@auth_bp.route("/signup/github")
def sign_up_github():
    session["origin_url"] = request.referrer
    if session.get("signup_state") is None:
        return redirect(url_for("auth.show_signup_form"))
    redirect_uri = url_for("auth.authorize_github", _external=True, flow="signup")
    return github.authorize_redirect(redirect_uri)


@auth_bp.route("/login/github")
def login_github():
    session["origin_url"] = request.referrer
    redirect_uri = url_for("auth.authorize_github", _external=True, flow="login")
    return github.authorize_redirect(redirect_uri)


@auth_bp.route("/authorize/github")
def authorize_github():
    origin_url = session.pop("origin_url", None)
    flow = request.args.get("flow")
    if (
        not flow
        or (flow not in ["signup", "login"])
        or (flow == "signup" and session.get("signup_state") is None)
        or (flow == "login" and session.get("login_state") is None)
    ):
        if "/dataset/upload" in origin_url:
            return redirect(origin_url)
        else:
            redirect(url_for("public.index"))

    # Autorizamos el token y obtenemos la información del usuario
    github.authorize_access_token()
    token = github.token["access_token"]
    session["github_token"] = token
    resp = github.get("user")
    profile = resp.json()

    # Obtener email si no está en el perfil principal
    if "email" not in profile or not profile["email"]:
        emails_resp = github.get("user/emails")
        profile["email"] = next(
            (
                email_data["email"]
                for email_data in emails_resp.json()
                if email_data.get("primary") and email_data.get("verified")
            ),
            None,
        )

    # Si no contiene el email
    if not profile.get("email"):
        return render_template(
            "auth/login_form.html",
            form=LoginForm(),
            error="Email not available from GitHub",
        )

    # Verificar si el usuario ya está registrado
    user = authentication_service.get_by_email(profile["email"])

    if user:
        # Comprobar si el usuario tiene GitHub como proveedor OAuth
        is_github_user = next(
            (
                provider
                for provider in user.oauth_providers
                if provider.provider_name == "github"
            ),
            None,
        )

        if not is_github_user:
            # Si el usuario ya existe pero no tiene GitHub vinculado, vinculamos la cuenta
            authentication_service.append_oauth_provider(user, "github", profile["id"])
        # En cualquier caso, si el usuario ya está registrado, hacemos login
        login_user(user, remember=True)
        if "/dataset/upload" in origin_url:
            return redirect(f"{origin_url}#githubToken={token}")
        else:
            return redirect(url_for("public.index") + f"#githubToken={token}")
    else:
        # Crear una nueva cuenta si el usuario no existe
        random_password = generate_random_password()
        hashed_password = generate_password_hash(random_password)
        name = profile.get("name", profile.get("login", "No name"))
        surname = profile.get("family_name", "No Surname")
        user = authentication_service.create_with_profile_and_oauth_provider_appended(
            email=profile["email"],
            password=hashed_password,
            name=name,
            surname=surname,
            oauth_provider="github",
            oauth_provider_user_id=profile["id"],
        )

        if "/dataset/upload" in origin_url:
            return redirect(f"{origin_url}#githubToken={token}")
        else:
            return redirect(url_for("public.index") + f"#githubToken={token}")


@auth_bp.route("/github/repositories", methods=["GET"])
def get_github_repositories():
    token = session.get("github_token")
    if not token:
        return jsonify({"error": "No authentication token found"}), 401

    headers = {"Authorization": f"token {token}"}
    params = {"affiliation": "owner,collaborator,organization_member"}
    response = requests.get(
        "https://api.github.com/user/repos", headers=headers, params=params, timeout=10
    )

    if response.status_code != 200:
        return jsonify({"error": "Failed to fetch repositories"}), response.status_code

    repos = response.json()
    repo_list = [
        {"id": repo["id"], "name": repo["name"], "full_name": repo["full_name"]}
        for repo in repos
    ]
    return jsonify(repo_list)


@auth_bp.route("/signup/gitlab")
def sign_up_gitlab():
    if session.get("signup_state") is None:
        return redirect(url_for("auth.show_signup_form"))
    redirect_uri = url_for("auth.authorize_gitlab", _external=True, flow="signup")
    return gitlab.authorize_redirect(redirect_uri)


@auth_bp.route("/login/gitlab")
def login_gitlab():
    session["origin_url"] = request.referrer
    redirect_uri = url_for("auth.authorize_gitlab", _external=True, flow="login")
    return gitlab.authorize_redirect(redirect_uri)


@auth_bp.route("/authorize/gitlab")
def authorize_gitlab():
    origin_url = session.pop("origin_url", None)
    flow = request.args.get("flow")
    if (
        not flow
        or (flow not in ["signup", "login"])
        or (flow == "signup" and session.get("signup_state") is None)
        or (flow == "login" and session.get("login_state") is None)
    ):
        if "/dataset/upload" in origin_url:
            return redirect(origin_url)
        else:
            return redirect(url_for("public.index"))

    gitlab.authorize_access_token()
    token = gitlab.token["access_token"]
    session["gitlab_token"] = token
    resp = gitlab.get("user")
    profile = resp.json()

    # Obtener email si no está en el perfil principal
    if "email" not in profile or not profile["email"]:
        emails_resp = gitlab.get("user/emails")
        profile["email"] = next(
            (
                email_data["email"]
                for email_data in emails_resp.json()
                if email_data.get("primary") and email_data.get("confirmed")
            ),
            None,
        )

    if not profile.get("email"):
        session.pop("signup_state", None)
        session.pop("login_state", None)
        return render_template(
            (
                "auth/show_signup_form.html"
                if flow == "signup"
                else "auth/login_form.html"
            ),
            form=SignupForm() if flow == "signup" else LoginForm(),
            error="Email not available from GitLab",
        )

    user = authentication_service.get_by_email(profile["email"])

    if user:
        is_gitlab_user = next(
            (
                provider
                for provider in user.oauth_providers
                if provider.provider_name == "gitlab"
            ),
            None,
        )
        if user.is_oauth_user():
            # Si el usuario ya existe en la base de datos y es OAuth, añadir una nueva conexión GitLab si esta no existe
            if not is_gitlab_user and flow == "signup":
                authentication_service.append_oauth_provider(
                    user, "gitlab", profile["id"]
                )

            login_user(user, remember=True)
            if "/dataset/upload" in origin_url:
                return redirect(f"{origin_url}#gitlabToken={token}")
            else:
                return redirect(url_for("public.index"))

        session.pop("signup_state", None)
        session.pop("login_state", None)
        return render_template(
            (
                "auth/show_signup_form.html"
                if flow == "signup"
                else "auth/login_form.html"
            ),
            form=SignupForm() if flow == "signup" else LoginForm(),
            error="Email already in use",
        )

    # Crear usuario si no existe
    random_password = generate_random_password()
    hashed_password = generate_password_hash(random_password)
    name = profile.get(
        "name",
        "No name" if profile.get("username") is None else profile.get("username"),
    )
    surname = profile.get("last_name", "No Surname")
    user = authentication_service.create_with_profile_and_oauth_provider_appended(
        email=profile["email"],
        password=hashed_password,
        name=name,
        surname=surname,
        oauth_provider="gitlab",
        oauth_provider_user_id=profile["id"],
    )

    login_user(user, remember=True)
    session.pop("signup_state", None)
    session.pop("login_state", None)
    if "/dataset/upload" in origin_url:
        return redirect(f"{origin_url}#gitlabToken={token}")
    else:
        return redirect(url_for("public.index"))


@auth_bp.route("/gitlab/repositories", methods=["GET"])
def get_gitlab_repositories():
    token = session.get("gitlab_token")
    if not token:
        return jsonify({"error": "No authentication token found"}), 401

    headers = {"Authorization": f"Bearer {token}"}
    response = requests.get(
        "https://gitlab.com/api/v4/projects",
        headers=headers,
        params={"membership": True},
        timeout=10,
    )

    if response.status_code != 200:
        return jsonify({"error": "Failed to fetch repositories"}), response.status_code

    repos = response.json()
    repo_list = [
        {
            "id": repo["id"],
            "name": repo["name"],
            "full_name": repo["path_with_namespace"],
        }
        for repo in repos
    ]
    return jsonify(repo_list)


@auth_bp.route("/logout")
def logout():
    logout_user()
    return redirect(url_for("public.index"))

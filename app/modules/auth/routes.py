from flask import render_template, redirect, render_template_string, session, url_for, request
from flask_login import current_user, login_user, logout_user
import requests

from app.modules.auth import auth_bp
from app.modules.auth.forms import SignupForm, LoginForm
from app.modules.auth.services import AuthenticationService
from app.modules.profile.services import UserProfileService


authentication_service = AuthenticationService()
user_profile_service = UserProfileService()


@auth_bp.route("/signup/", methods=["GET", "POST"])
def show_signup_form():
    if current_user.is_authenticated:
        return redirect(url_for('public.index'))

    form = SignupForm()
    if form.validate_on_submit():
        email = form.email.data
        if not authentication_service.is_email_available(email):
            return render_template("auth/signup_form.html", form=form, error=f'Email {email} in use')

        try:
            user = authentication_service.create_with_profile(**form.data)
        except Exception as exc:
            return render_template("auth/signup_form.html", form=form, error=f'Error creating user: {exc}')

        # Log user
        login_user(user, remember=True)
        return redirect(url_for('public.index'))

    return render_template("auth/signup_form.html", form=form)


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


# Recuperación del token de la ventana emergente de autenticación
@auth_bp.route('/auth/callback/github')
def github_callback():
    code = request.args.get('code')
    token = authentication_service.exchange_code_for_token(code, 'github')
    session['github_token'] = token
    return render_template_string("""
        <script>
            window.close();
            window.opener.postMessage({{ '{' }}githubToken: '{{ token }}'{{ '}' }}, "*");
        </script>
    """, token=token)


# Recuperación del token de la ventana emergente de autenticación
@auth_bp.route('/auth/callback/gitlab')
def gitlab_callback():
    code = request.args.get('code')
    token = authentication_service.exchange_code_for_token(code, 'gitlab')
    session['gitlab_token'] = token
    return render_template_string("""
        <script>
            window.close();
            window.opener.postMessage({{ '{' }}gitlabToken: '{{ token }}'{{ '}' }}, "*");
        </script>
    """, token=token)


@auth_bp.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('public.index'))

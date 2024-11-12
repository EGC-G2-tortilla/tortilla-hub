import os
from flask_login import login_user
from flask_login import current_user
import requests

from app.modules.auth.models import User
from app.modules.auth.repositories import UserRepository
from app.modules.profile.models import UserProfile
from app.modules.profile.repositories import UserProfileRepository
from core.configuration.configuration import uploads_folder_name
from core.services.BaseService import BaseService


class AuthenticationService(BaseService):
    def __init__(self):
        super().__init__(UserRepository())
        self.user_profile_repository = UserProfileRepository()

    def login(self, email, password, remember=True):
        user = self.repository.get_by_email(email)
        if user is not None and user.check_password(password):
            login_user(user, remember=remember)
            return True
        return False

    def is_email_available(self, email: str) -> bool:
        return self.repository.get_by_email(email) is None
    
    def get_by_email(self, email: str) -> User:
        return self.repository.get_by_email(email)

    def create_with_profile(self, **kwargs):
        try:
            email = kwargs.pop("email", None)
            password = kwargs.pop("password", None)
            name = kwargs.pop("name", None)
            surname = kwargs.pop("surname", None)

            if not email:
                raise ValueError("Email is required.")
            if not password:
                raise ValueError("Password is required.")
            if not name:
                raise ValueError("Name is required.")
            if not surname:
                raise ValueError("Surname is required.")

            user_data = {
                "email": email,
                "password": password
            }

            profile_data = {
                "name": name,
                "surname": surname,
            }

            user = self.create(commit=False, **user_data)
            profile_data["user_id"] = user.id
            self.user_profile_repository.create(**profile_data)
            self.repository.session.commit()
        except Exception as exc:
            self.repository.session.rollback()
            raise exc
        return user

    def create_with_profile_and_oauth_provider_appended(self, **kwargs):
        try:
            email = kwargs.pop("email", None)
            password = kwargs.pop("password", None)
            name = kwargs.pop("name", None)
            surname = kwargs.pop("surname", None)
            oauth_provider = kwargs.pop("oauth_provider", None)
            oauth_provider_user_id = kwargs.pop("oauth_provider_user_id", None)

            if not email:
                raise ValueError("Email is required.")
            if not name:
                raise ValueError("Name is required.")
            if not surname:
                raise ValueError("Surname is required.")
            if not oauth_provider:
                raise ValueError("OAuth provider is required.")
            if not oauth_provider_user_id:
                raise ValueError("OAuth provider user ID is required.")

            user_data = {
                "email": email,
                "password": password
            }

            profile_data = {
                "name": name,
                "surname": surname,
            }

            user = self.create(commit=False, **user_data)
            profile_data["user_id"] = user.id
            self.user_profile_repository.create(**profile_data)
            self.repository.session.commit()

            oauth_provider_data = {
                "user": user,
                "provider_name": oauth_provider,
                "provider_user_id": oauth_provider_user_id
            }
            self.repository.create_oauth_provider(**oauth_provider_data)
            self.repository.session.commit()
        except Exception as exc:
            self.repository.session.rollback()
            raise exc
        return user

    def update_profile(self, user_profile_id, form):

        if form.validate():
            updated_instance = self.update(user_profile_id, **form.data)
            return updated_instance, None

        return None, form.errors

    def get_authenticated_user(self) -> User | None:
        if current_user.is_authenticated:
            return current_user
        return None

    def get_authenticated_user_profile(self) -> UserProfile | None:
        if current_user.is_authenticated:
            return current_user.profile
        return None

    def temp_folder_by_user(self, user: User) -> str:
        return os.path.join(uploads_folder_name(), "temp", str(user.id))

    # Cambia el codigo devuelto por un access token para cada usuario
    def exchange_code_for_token(self, code, platform):
        if platform == 'github':
            url = "https://github.com/login/oauth/access_token"
            data = {
                'client_id': 'Ov23liirdMyilGskGdbL',
                'client_secret': '1a272cbe8559532aaef5d017c94871fc09cf8dd6',
                'code': code
            }
        elif platform == 'gitlab':
            url = "https://gitlab.com/oauth/token"
            data = {
                'client_id': 'TU_CLIENT_ID_GITLAB',
                'client_secret': 'TU_CLIENT_SECRET_GITLAB',
                'code': code,
                'grant_type': 'authorization_code',
                'redirect_uri': 'https://tu_dominio.com/auth/callback/gitlab'
            }
        headers = {'Accept': 'application/json'}
        response = requests.post(url, data=data, headers=headers)
        return response.json().get('access_token')

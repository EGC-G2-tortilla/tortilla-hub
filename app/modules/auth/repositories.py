from app.modules.auth.models import User
from core.repositories.BaseRepository import BaseRepository
from app.modules.auth.models import OAuthProvider


class UserRepository(BaseRepository):
    def __init__(self):
        super().__init__(User)

    def create(self, commit: bool = True, **kwargs):
        password = kwargs.pop("password")
        instance = self.model(**kwargs)
        instance.set_password(password)
        self.session.add(instance)
        if commit:
            self.session.commit()
        else:
            self.session.flush()
        return instance

    def get_by_email(self, email: str):
        return self.model.query.filter_by(email=email).first()

    def create_oauth_provider(self, user, provider_name, provider_user_id):
        oauth_provider = OAuthProvider(user=user, provider_name=provider_name, provider_user_id=provider_user_id)
        self.session.add(oauth_provider)
        self.session.commit()
        return oauth_provider

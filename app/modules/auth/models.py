from datetime import datetime, timezone

from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from app.modules.community.models import user_community_table
from app import db


class OAuthProvider(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    provider_name = db.Column(db.String(50))  # 'google', 'github', etc.
    provider_user_id = db.Column(
        db.String(100), unique=True
    )  # ID del usuario en el proveedor


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)

    email = db.Column(db.String(256), unique=True, nullable=False)
    password = db.Column(db.String(256), nullable=False)
    created_at = db.Column(
        db.DateTime, nullable=False, default=lambda: datetime.now(timezone.utc)
    )
    orcid = db.Column(db.String(19), unique=True, nullable=True)

    data_sets = db.relationship("DataSet", backref="user", lazy=True)
    profile = db.relationship("UserProfile", backref="user", uselist=False)
    communities = db.relationship(
        "Community", secondary=user_community_table, back_populates="members"
    )
    oauth_providers = db.relationship("OAuthProvider", backref="user", lazy=True)

    def __init__(self, **kwargs):
        super(User, self).__init__(**kwargs)
        if "password" in kwargs:
            self.set_password(kwargs["password"])
        if "password" in kwargs:
            self.set_password(kwargs["password"])

    def __repr__(self):
        return f"<User {self.email}>"
        return f"<User {self.email}>"

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)

    def temp_folder(self) -> str:
        from app.modules.auth.services import AuthenticationService

        return AuthenticationService().temp_folder_by_user(self)

    def is_oauth_user(self):
        "Método que indica si el usuario se ha registrado mediante un proveedor OAuth"
        return len(self.oauth_providers) > 0

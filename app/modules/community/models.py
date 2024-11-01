from app import db


class Community(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True, nullable=False)
    url = db.Column(db.String(255), nullable=False)
    description = db.Column(db.Text, nullable=True)
    # TODO: add tags
    # TODO: add users

    def __repr__(self):
        return f'Community<{self.id}>'

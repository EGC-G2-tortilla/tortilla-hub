from app import db


user_community_table = db.Table('user_community',
                                db.Column('user_id', db.Integer, db.ForeignKey('user.id'), primary_key=True),
                                db.Column('community_id', db.Integer, db.ForeignKey('community.id'), primary_key=True))


class Community(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True, nullable=False)
    url = db.Column(db.String(255), nullable=False)
    description = db.Column(db.Text, nullable=True)
    admin = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    members = db.relationship('User', secondary=user_community_table, back_populates='communities')

    def __repr__(self):
        return f'Community<{self.id}>'

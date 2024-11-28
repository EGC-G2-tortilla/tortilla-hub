from app import db


class CommunityJoinRequest(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    def __repr__(self):
        return f'CommunityJoinRequest<{self.id}>'

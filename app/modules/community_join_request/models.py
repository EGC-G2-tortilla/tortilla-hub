from app import db


class CommunityJoinRequest(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_who_wants_to_join_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    community_id = db.Column(db.Integer, db.ForeignKey("community.id"), nullable=True)

    def delete(self):
        db.session.delete(self)
        db.session.commit()
        
    def __repr__(self):
        return f'CommunityJoinRequest<{self.id}>'

from app import db
from datetime import datetime


class Fakenodo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(128))
    description = db.Column(db.Text)
    dataset_id = db.Column(db.Integer, db.ForeignKey("data_set.id"), nullable=False)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.now)

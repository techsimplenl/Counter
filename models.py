"""Counter MODULE"""
from app import db

class Counter(db.models):
    """Counter class MODEL"""
    id = db.Column(db.Integer, primary_key=True)
    counter = db.Column(db.Integer, nullable=False)
    
"""Counter MODULE"""
# models.py
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Counter(db.Model):
    """Counter class MODEL"""
    id = db.Column(db.Integer, primary_key=True,autoincrement=True)
    initial_value = db.Column(db.Integer, nullable=False)
    counter = db.Column(db.Integer, nullable=False)
    
"""Counter MODULE"""
# models.py
from flask_sqlalchemy import SQLAlchemy
# Create an instance of the SQLAlchemy class
db = SQLAlchemy()

class Counter(db.Model):
    """This class defines the structure of the 'Counter' table in the database."""
    id = db.Column(db.Integer, primary_key=True,autoincrement=True)
    initial_value = db.Column(db.Integer, nullable=False)
    counter = db.Column(db.Integer, nullable=False)
    
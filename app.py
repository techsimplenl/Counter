"""APP MODULE"""
import os
from dotenv import load_dotenv
from flask import Flask
from gunicorn import FlaskApplication  # Import the FlaskApplication class from gunicorn
from api.counter import counter_bp
from models import db

load_dotenv()

import sys
print(sys.path)

def create_app():
    """CREATE APP"""
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv("DATABASE_URI")
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SECRET_KEY'] = os.getenv("SECRET_KEY")
    db.init_app(app)
    # Ensure that the database connection is closed after each request
    @app.after_request
    def after_request(response):
        db.session.close()
        return response
    # Register the counter blueprint
    app.register_blueprint(counter_bp)
    return app

if __name__ == '__main__':
    app = create_app()
    with app.app_context():
        db.create_all()
    # Run the application using Gunicorn
    FlaskApplication(web_app,gunicorn_options={"workers": os.getenv("WORKERS"),"bind":os.getenv("BIND")}).run()
    
"""APP MODULE"""
import os
from dotenv import load_dotenv
from flask import Flask
from server.gunicorn_conf import FlaskApplication  # Import the FlaskApplication class from gunicorn
from services.check_if_table_exist import check_if_table_exists
from services.read_row_from_db import read_row_from_db
from api.counter import counter_bp
from api.models import db

load_dotenv()

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

app = create_app()

# check if the database and drop it if it exists
check_if_table_exists(os.getenv("DATABASE_URI"))
# Create the database tables
with app.app_context():
    db.create_all()


if __name__ == '__main__':
    gunicorn_options = {
        "workers": 4,
        "bind": "0.0.0.0:8000",
        # Add more Gunicorn options as needed
    }
    
    FlaskApplication(app, options=gunicorn_options).run()
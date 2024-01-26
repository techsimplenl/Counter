"""APP MODULE"""

import os
from dotenv import load_dotenv
from flask import Flask
from server.gunicorn_conf import CounterApplication
from services.check_if_table_exist import check_if_table_exists
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
        "workers": 4, # Optional 4 workers what means number of worker processses to use this process
        "bind": "0.0.0.0:8000",
        # Add more Gunicorn options as needed
    }
    CounterApplication(app, options=gunicorn_options).run()
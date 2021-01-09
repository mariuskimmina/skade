import json
import logging
from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()
migrate = Migrate()
login_manager = LoginManager()

def create_app(test_config=None):
    app = Flask(__name__)

    if test_config is None:
        with open('config/default.json')as f:
            config = json.load(f)
        app.config.update(config)
    else:
        app.config.from_mapping(test_config)

    login_manager.init_app(app)
    db.init_app(app)
    migrate.init_app(app, db)

    #Disalbe the "Please login to view this page" message
    login_manager.login_message = u""

    from .upload import upload
    from .auth import auth
    from .models import User

    app.register_blueprint(upload)
    app.register_blueprint(auth)

    login_manager.login_view = "auth.login_screen"

    return app

if __name__ == "__main__":
    app = create_app()
    app.run()
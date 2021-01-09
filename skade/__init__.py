import json
import logging
from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy

def create_app(test_config=None):
    app = Flask(__name__)
    login_manager = LoginManager()
    db = SQLAlchemy()

    if test_config is None:
        with open('config/default.json')as f:
            config = json.load(f)
        app.config.update(config)
    else:
        app.config.from_mapping(test_config)

    login_manager.init_app(app)
    db.init_app(app)

    #Disalbe the "Please login to view this page" message
    login_manager.login_message = u""

    from .upload import upload
    from .auth import auth

    app.register_blueprint(upload)
    app.register_blueprint(auth)

    login_manager.login_view = "auth.login_screen"

    return app

if __name__ == "__main__":
    app = create_app()
    app.run()
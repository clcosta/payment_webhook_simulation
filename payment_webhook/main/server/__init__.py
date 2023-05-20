__all__ = ['app']

from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy

from payment_webhook.data import DataBase
from payment_webhook.infra.settings import (
    DATABASE_URL,
    ENCRYPTION_KEY,
    TEMPLATE_DIR,
)

from .routes import *

db = SQLAlchemy()

app = Flask(__name__, template_folder=TEMPLATE_DIR)


login_manager = LoginManager()
login_manager.login_view = 'pages.login'
login_manager.init_app(app)

app.secret_key = ENCRYPTION_KEY
app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URL

app.register_blueprint(webhook_router)
app.register_blueprint(pages_router)


@login_manager.user_loader
def user_loader(user_id: str):
    with DataBase() as database:
        user = database.get_user(user_id=user_id)
        return user

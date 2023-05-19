__all__ = ['app']

from flask import Flask
from flask_login import LoginManager

from payment_webhook.data import DataBase
from payment_webhook.infra.settings import ENCRYPTION_KEY, TEMPLATE_DIR

from .routes import *

app = Flask(__name__, template_folder=TEMPLATE_DIR)

login_manager = LoginManager()
login_manager.login_view = 'pages.login'
login_manager.init_app(app)

app.secret_key = ENCRYPTION_KEY

app.register_blueprint(webhook_router)
app.register_blueprint(pages_router)


@login_manager.user_loader
def user_loader(email: str):
    print('Este é o email', email)
    with DataBase() as db:
        user = db.get_user(email=email)
        return user


#
# @login_manager.request_loader
# def request_loader(request):
#     email = request.form.get('email')
#     if not email:
#         print('retornando vazio')
#         return None
#     with DataBase() as db:
#         user = db.get_user()
#         print('retornando user', user)
#         return user

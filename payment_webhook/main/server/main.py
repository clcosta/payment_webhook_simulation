from flask import Flask
from flask_restful import Api
from payment_webhook.settings import TEMPLATE_DIR
from .routes import *

app = Flask(__name__, template_folder=TEMPLATE_DIR)
api = Api(app)

app.register_blueprint(webhook_router)
app.register_blueprint(pages_router)
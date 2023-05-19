from flask import Blueprint

from payment_webhook.application.controllers import WebHookCallbackController

webhook_router = Blueprint('webhook', __name__, url_prefix='/webhook')


@webhook_router.route('/callback', methods=['POST'])
def callback():
    return WebHookCallbackController().handle()

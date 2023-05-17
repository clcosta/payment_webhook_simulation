from flask import Blueprint

webhook_router = Blueprint('webhook', __name__, url_prefix='/webhook')


@webhook_router.route('/callback', methods=['POST'])
def callback():
    print(request.json())
    return "Success"
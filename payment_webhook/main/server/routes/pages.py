from flask import Blueprint
from flask_login import login_required

from payment_webhook.application.controllers import (
    HomeController,
    UserAuthenticationController,
    UserLogoutController,
    UserRegisterController,
)

pages_router = Blueprint('pages', __name__)


@pages_router.route('/', methods=['GET'])
@login_required
def home():
    return HomeController().handle()


@pages_router.route('/register', methods=['GET', 'POST'])
def register():
    return UserRegisterController().handle()


@pages_router.route('/login', methods=['GET', 'POST'])
def login():
    return UserAuthenticationController().handle()


@pages_router.route('/logout', methods=['GET'])
@login_required
def logout():
    return UserLogoutController().handle()

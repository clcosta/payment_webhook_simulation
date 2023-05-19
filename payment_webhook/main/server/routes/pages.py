from flask import Blueprint, redirect, render_template, request, url_for
from flask_login import login_required

from payment_webhook.application.controllers import (
    UserAuthenticationController,
    UserRegisterController,
)

pages_router = Blueprint('pages', __name__)


@pages_router.route('/', methods=['GET'])
@login_required
def home():
    return render_template('home.html')


@pages_router.route('/register', methods=['GET', 'POST'])
def register():
    return UserRegisterController().handle()


@pages_router.route('/login', methods=['GET', 'POST'])
def login():
    return UserAuthenticationController().handle()


@pages_router.route('/logout', methods=['GET'])
def logout():
    return redirect(url_for('pages.home'))

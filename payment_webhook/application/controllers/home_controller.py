from flask import render_template
from flask_login import current_user

from payment_webhook.data import DataBase

from .base_controller import BaseController


class HomeController(BaseController):
    def get(self):
        user = current_user
        with DataBase() as db:
            history = db.user_payment_history(user_id=user.id)
        return render_template('home.html', history=history)

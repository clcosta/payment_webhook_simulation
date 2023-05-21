import json

from flask import render_template
from flask_login import current_user

from payment_webhook.data import DataBase

from .base_controller import BaseController


class HomeController(BaseController):
    def get(self):
        user = current_user
        with DataBase() as db:
            user_history = db.user_payment_history(user_id=user.id)
            for history in user_history:
                history.info = json.loads(history.info)
        return render_template('home.html', user_history=user_history)

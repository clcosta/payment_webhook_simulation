from flask import render_template

from .base_controller import BaseController


class HomeController(BaseController):
    def get(self):
        return render_template('register.html')

    def post(self):
        return self._formating_json_response(
            405, {'message': 'Method not allowed'}
        )

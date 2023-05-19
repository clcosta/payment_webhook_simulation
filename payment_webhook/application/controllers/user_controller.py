from flask import flash, redirect, render_template, request

from .base_controller import BaseController


class UserRegisterController(BaseController):
    def get(self):
        return render_template('register.html')

    def post(self):
        flash('POST METHOD NOT IMPLEMENTED YET')
        return render_template('register.html')


class UserAuthenticationController(BaseController):
    def get(self):
        return render_template('login.html')

    def post(self):
        flash('POST METHOD NOT IMPLEMENTED YET')
        return render_template('login.html')

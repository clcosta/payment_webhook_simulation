from flask import flash, redirect, render_template, request, url_for
from flask_login import current_user, login_user, logout_user

from payment_webhook.data import DataBase
from payment_webhook.infra.settings import DEFAULT_REGISTER_TOKEN

from .base_controller import BaseController


class UserRegisterController(BaseController):
    def get(self):
        return render_template('register.html')

    def post(self):
        email = request.form.get('email')
        password = request.form.get('password')
        access_token = request.form.get('access_token', default='NULL').upper()

        with DataBase() as db:
            user_exists = db.exists_user(email=email)
            if user_exists:
                flash('Email já existe!', 'danger')
                return redirect(url_for('pages.login'))

            if len(password) <= 5:
                flash('Senha muito curta!', 'danger')
                return redirect(url_for('pages.register'))

            if access_token.strip() != DEFAULT_REGISTER_TOKEN.upper().strip():
                flash(
                    'Token de acesso não corresponde a um token válido!',
                    'danger',
                )
                return redirect(url_for('pages.register'))

            user = db.register_user(
                email=email,
                password=password,  # The password is already encrypted
            )

            flash(f'Usuário {user.nome} registrado com sucesso!')
            return redirect(url_for('pages.login'))


class UserAuthenticationController(BaseController):
    def get(self):
        return render_template('login.html')

    def post(self):

        email = request.form.get('email')
        password = request.form.get('password')

        with DataBase() as db:
            try:
                user = db.get_registered_user(email=email, password=password)
                if not user:
                    flash(
                        'Email/senha incorreto ou usuário não registrado!',
                        'danger',
                    )
                    return redirect(url_for('pages.login'))

                login_user(user)
                return redirect(url_for('pages.home'))
            except ValueError as er:
                flash(f'Falha ao realizar login: {er}', 'danger')
                return redirect(url_for('pages.login'))
            except Exception as er:
                flash(f'Erro inesperado ao realizar login: {er}', 'danger')
                return redirect(url_for('pages.login'))


class UserLogoutController(BaseController):
    def get(self):
        logout_user()
        return redirect(url_for('pages.login'))

from flask import flash, make_response, redirect, render_template, request, url_for
from flask_login import current_user, login_required, login_user, logout_user
from flask_restful import Resource
from {{cookiecutter.app_name}}.ext.auth.models import User

__all__ = (
    "Home",
    "Login",
    "Logout",
)


class Home(Resource):
    def get(self, route=None):
        headers = {"Content-Type": "text/html"}
        if current_user.is_authenticated and current_user.permission_id == 1:
            return redirect(url_for("admin.index"))
        return make_response(render_template("index.html"), 200, headers)


class Login(Resource):
    def get(self, *args):
        headers = {"Content-Type": "text/html"}
        return make_response(render_template("login.html"), 200, headers)

    def post(self):
        email = request.form.get("email")
        pwd = request.form.get("password")
        remember = request.form.get("remember")

        user = User.query.filter_by(email=email).first()

        if not user or not user.verify_password(pwd):
            flash("Usuário ou senha invalidos", category="warning")
            return redirect(url_for("website.login"))

        login_user(user, remember=remember)
        return redirect(url_for("website.home"))


class Logout(Resource):
    @login_required
    def get(self):
        logout_user()
        return redirect(url_for("website.login"))

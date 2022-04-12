from flask_restful import Api
from {{cookiecutter.app_name}}.ext.api.views.website import Home, Login, Logout


def init_site_routes(site):
    Web = Api(site)
    Web.add_resource(Home, "/", endpoint="home")
    Web.add_resource(Login, "/login", endpoint="login")
    Web.add_resource(Logout, "/logout", endpoint="logout")

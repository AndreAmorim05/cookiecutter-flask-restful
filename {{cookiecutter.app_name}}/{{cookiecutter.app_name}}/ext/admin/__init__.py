from flask_admin import Admin
from {{cookiecutter.app_name}}.ext.auth.models import Permission, User
from {{cookiecutter.app_name}}.ext.db import db
from {{cookiecutter.app_name}}.ext.db.models import *

from .admin import PermissionAdmin, UserAdmin

admin = Admin()


def init_app(app):
    admin.init_app(app)
    admin.name = app.config.get("ADMIN_NAME", "PREDITIVO")
    admin.template_mode = app.config.get("ADMIN_TEMPLATE_MODE", "bootstrap4")
    admin.add_view(UserAdmin(User, db.session))
    admin.add_view(PermissionAdmin(Permission, db.session))

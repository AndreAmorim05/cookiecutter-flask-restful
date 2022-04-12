from flask import abort, flash
from flask_admin.actions import action
from flask_admin.contrib.sqla import ModelView
from flask_login import current_user
from {{cookiecutter.app_name}}.ext.auth.models import Permission, User


def format_permission(self, request, user, *args):
    perm_name = (
        Permission.query.with_entities(Permission.permission)
        .filter_by(id=user.permission)
        .first()[0]
    )
    return f"( {user.permission} ) - " + perm_name


def format_datetime(self, request, instance, *args):

    dt = getattr(instance, args[0])
    if dt:
        return dt.strftime("%d/%m/%Y  -  %H:%M:%S %z")
    return dt


def format_date(self, request, instance, *args):

    dt = getattr(instance, args[0])
    if dt:
        return dt.strftime("%d/%m/%Y")
    return dt


class BaseView(ModelView):
    def is_accessible(self):
        if current_user.is_authenticated and current_user.permission_id == 1:
            print(current_user.is_authenticated, current_user.permission_id)
            return True
        else:
            abort(403)


class PermissionAdmin(BaseView):
    can_delete = False
    column_list = ["permission"]


class UserAdmin(BaseView):
    column_formatters = {
        "permission_id": format_permission,
    }

    column_exclude_list = [
        "password",
    ]

    can_delete = False
    can_edit = True
    can_create = True

    column_searchable_list = ["name", "email"]

    column_filters = ["name", "email", "permission_id"]

    column_editable_list = ["name", "email"]

    @action("password_recover", "Send passoword recover link", "Are you sure?")
    def pass_recover(self, ids):
        users = User.query.filter(User.id.in_(ids)).all()
        flash(
            f"{len(users)} emails enviados para recuperação de senha",
            "success",
        )

from flask_login import UserMixin
from werkzeug.security import check_password_hash, generate_password_hash
from {{cookiecutter.app_name}}.ext.auth import login_manager
from {{cookiecutter.app_name}}.ext.db import db


@login_manager.user_loader
def get_user(user_id):
    return User.query.filter_by(id=user_id).first()


class Permission(db.Model):
    __tablename__ = "permissions"
    id = db.Column(
        "id", db.Integer, primary_key=True, nullable=False, autoincrement=True
    )
    permission = db.Column("permission", db.String(50), nullable=False)

    def __repr__(self) -> str:
        return f"< Permission(id={self.id}, permission={self.permission})"


class User(db.Model, UserMixin):
    __tablename__ = "user"
    id = db.Column(
        "id", db.Integer, primary_key=True, nullable=False, autoincrement=True
    )
    name = db.Column("name", db.String(255), nullable=False)
    email = db.Column("email", db.String(84), nullable=False, unique=True)
    password = db.Column("password", db.String(128), nullable=False)
    permission_id = db.Column(
        "permission_id",
        db.Integer,
        db.ForeignKey("permissions.id"),
        nullable=False,
    )

    permission = db.relationship("Permission", foreign_keys=permission_id)

    def __init__(self, name, email, password, permission_id):
        self.name = name
        self.email = email
        self.password = generate_password_hash(password)
        self.permission_id = permission_id

    def verify_password(self, pwd):
        return check_password_hash(self.password, pwd)

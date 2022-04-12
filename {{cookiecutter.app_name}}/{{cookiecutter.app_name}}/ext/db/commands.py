import click
from {{cookiecutter.app_name}}.ext.auth.models import Permission, User
from {{cookiecutter.app_name}}.ext.db import db


def create_db():
    """Creates database"""
    db.create_all()


def drop_db():
    """Cleans database"""
    db.drop_all()


def populate_db():
    """Populate db with sample data"""
    try:
        data = [
            Permission(permission="admin"),
            User(
                name="{{ cookiecutter.author_name }}",
                email="{{ cookiecutter.admin_access_email }}",
                password="{{ cookiecutter.admin_access_password }}",
                permission_id=1,
            ),
        ]
        db.session.bulk_save_objects(data)
        db.session.commit()

        click.echo("Populate done with success.")
        return User.query.all()
    except Exception as e:
        click.echo(e)

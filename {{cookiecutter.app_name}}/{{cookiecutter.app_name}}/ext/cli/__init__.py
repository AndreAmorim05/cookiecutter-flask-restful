import click
from {{cookiecutter.app_name}}.ext.auth.models import User
from {{cookiecutter.app_name}}.ext.db import db
from {{cookiecutter.app_name}}.ext.db.commands import create_db, drop_db, populate_db


def init_app(app):

    app.cli.add_command(app.cli.command()(create_db))
    app.cli.add_command(app.cli.command()(drop_db))
    app.cli.add_command(app.cli.command()(populate_db))

    @app.cli.command()
    @click.option("--name", "-n", help="Type the name of the user")
    @click.option("--email", "-e", help="Type the email of the user")
    @click.option("--password", "-p", help="Type the password of the user")
    @click.option("--company", "-c", help="Type the company of the user")
    @click.option("--role", "-r", help="Type the permission/role of the user")
    def add_user(name, email, password, company, role):
        try:
            user = User(
                name=name,
                email=email,
                password=password,
                company_id=company,
                permission_id=role,
            )
            db.session.add(user)
            db.session.commit()
            click.echo("Usuário adicionado")
        except Exception as e:
            click.echo(e)

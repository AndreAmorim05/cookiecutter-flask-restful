import typing

import sqlalchemy as sa
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
migrate = Migrate()


def repr(object, **fields: typing.Dict[str, typing.Any]) -> str:
    """
    Helper for __repr__
    Used to do the querys setted with the right sintaxe and an easy way to do it

    Example:

    class User(db.Model):
        __tablename__ = 'user'
        id = db.Column(db.Integer, primary_key=True)
        name = db.Column(db.String(50))
        phone_numb = db.Column(db.String(16))
        email = db.Column(db.String(50))

        def __repr__(self):
            return repr(self, id=self.id,
                        name=self.name,
                        phone_numb=self.phone_numb,
                        email=self.email)
    """
    field_strings = []
    at_least_one_attached_attribute = False
    for key, field in fields.items():
        try:
            field_strings.append(f"{key}={field!r}")
        except sa.orm.exc.DetachedInstanceError:
            field_strings.append(f"{key}=DetachedInstanceError")
        else:
            at_least_one_attached_attribute = True
    if at_least_one_attached_attribute:
        return f"<{object.__class__.__name__}({','.join(field_strings)})>"
    return f"<{object.__class__.__name__} {id(object)}>"


def init_app(app):
    db.init_app(app)
    migrate.init_app(app, db)

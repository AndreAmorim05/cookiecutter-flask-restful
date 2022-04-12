from collections import namedtuple

from flask import render_template
from flask_mail import Message
from {{cookiecutter.app_name}}.ext.celery.celery import celery
from {{cookiecutter.app_name}}.ext.mail import mail


def email_formater(subject, recipients, body=None, html=None, charset="utf-8"):
    Email = namedtuple("Email", "subject recipients body html charset")
    email = Email(subject, recipients, body, html, charset)
    return email._asdict()


@celery.task()
def send_email(
    email: str,
    subject: str,
    body: str,
):
    if isinstance(email, str):
        email = [email]
    msg = email_formater(subject, email, body=body)
    email = Message(**msg)
    mail.send(email)

from threading import Thread
from flask_mail import Message
from flask import current_app
import app
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
from app.resources.errors import InternalServerError
from app import celery

mail = SendGridAPIClient(current_app.config["SENDGRID_API_KEY"])


def send_async_email(app, msg):
    with app.app_context():
        try:
            mail.send(msg)
        except ConnectionRefusedError:
            raise InternalServerError("[MAIL SERVER] not working")


@celery.task(name="celery_flask_async_email")
def sendflask_email(subject, recipients, text_body, html_body):
    msg = Message(
        subject, sender=current_app.config["MAIL_DEFAULT_SENDER"], recipients=recipients
    )
    msg.body = text_body
    msg.html = html_body
    Thread(target=send_async_email, args=(current_app, msg)).start()


@celery.task(name="celery_async_email")
def send_email(subject, recipients, text_body, html_body):
    msg = Mail(
        from_email=current_app.config["MAIL_DEFAULT_SENDER"],
        to_emails=recipients,
        subject=subject,
        html_content=html_body,
    )
    response = mail.send(msg)
import os
from django.core.mail import send_mail
from django.apps import AppConfig
import requests
from dotenv import load_dotenv

load_dotenv()


class UsersConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'users'


def send_message(key, email):
    message = f"Hi there!\n\nYou was successfully registered at Acc.\n\n" \
              f"For the full operation of the service, you need to connect a telegram account to it.\n\n" \
              f"If this doesn't work copy and paste the following link into your browser:\n\n" \
              f"https://t.me/NikAccountantBot?start={key}\n\n" \
              f"Many thanks for your interest to our project."

    send_mail(
        'Registration at Acc',
        message,
        'd07c73b8-4a43-44e0-9e52-3549426d57ed@heroku.com',
        [email],
        fail_silently=True,
    )



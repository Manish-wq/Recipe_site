from home.models import Student
import time
from django.core.mail import send_mail, EmailMessage
from django.conf import settings

def send_email_to_client():
    subject = 'This email is from  the django server'
    message = 'Test message from serverr!'
    from_email = 'settings.EMAIL_HOST_USER'
    recipient_list =['victorvlog11m@gmail.com']
    send_mail(subject, message, from_email, recipient_list)


def send_email_with_attachment(subject, message, recipient_list, file_path):
    mail = EmailMessage(subject=subject, body=message, from_email= settings.EMAIL_HOST_USER, to = recipient_list)

    mail.attach_file(file_path)
    mail.send()
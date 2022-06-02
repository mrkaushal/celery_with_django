from django.contrib.auth import get_user_model
from django.core.mail import send_mail
from celery_with_django import settings
from celery import shared_task

@shared_task(bind=True)
def send_mail_func(self):
    #operations
    users = get_user_model().objects.all()
    for user in users:
        mail_subject = 'Hello, {}'.format(user.first_name)
        mail_body = 'This is a test mail {}'.format(user.last_name)
        to_email = user.email
        send_mail(
            subject=mail_subject,
            message=mail_body, 
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[to_email],
            fail_silently=True
        )
    return "Done"
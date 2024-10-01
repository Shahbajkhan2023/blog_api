from celery import shared_task
from django.core.mail import send_mail
from django.contrib.auth.models import User

@shared_task
def send_email_to_users(post_title):
    users = User.objects.all()  # Sabhi users ko nikaal rahe hain
    emails = [user.email for user in users if user.email]  # Emails ka list bana rahe hain

    send_mail(
        subject='New Post Created',
        message=f'A new post titled "{post_title}" has been created.',
        from_email='shbkhan@bestpeers.com',  # Yeh aapke email address ke sath replace karein
        recipient_list=emails,
        fail_silently=False,
    )

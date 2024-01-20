from django.core.mail import send_mail
from django.contrib.auth import get_user_model
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings

UserModel = get_user_model()

@receiver(post_save, sender=UserModel)
def notify_administrator(sender, instance, created, **kwargs):
    if created:
        subject = 'New User Registration Approval Needed'
        message = f'A new user ({instance.username}) has registered and requires approval.'
        from_email = settings.DEFAULT_FROM_EMAIL
        recipient_list = [admin_email for _, admin_email in settings.ADMINS]
        send_mail(subject, message, from_email, recipient_list)

from __future__ import unicode_literals

from django.db import models
from django.conf import settings
from django.dispatch import receiver
from django.core.mail import send_mail
from django.contrib.auth.models import User
from django.db.models.signals import post_save

class Account(models.Model):
    user = models.OneToOneField(User)
    wallet_address = models.CharField(max_length=35)

@receiver(post_save, sender=User)
def send_welcome_email(sender, **kwargs):
    user = kwargs['instance']
    update_fields = kwargs['update_fields']

    # Send email after user logs in and last_login attribute is updated.
    if update_fields is not None:
        send_mail(
            'Subject here',
            'Here is the message.',
            settings.DEFAULT_FROM_EMAIL,
            [user.email],
            fail_silently=False,
        )
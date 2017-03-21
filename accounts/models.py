from __future__ import unicode_literals

from django.db import models
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
    if user.first_name:
        send_mail(
            'Subject here',
            'Here is the message.',
            'from@example.com',
            ['alwaysdeone@gmail.com'],
            fail_silently=False,
        )
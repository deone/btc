from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

class Account(models.Model):
    user = models.OneToOneField(User)
    wallet_address = models.CharField(max_length=35)
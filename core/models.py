from __future__ import unicode_literals

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Plan(models.Model):
    name = models.CharField(max_length=25)
    min_deposit = models.DecimalField(max_digits=4, decimal_places=1)
    period = models.IntegerField()
    percentage_return = models.IntegerField()

    def __str__(self):
        return '%s - %s BTC' % (self.name, str(self.min_deposit))

class Investment(models.Model):
    user = models.ForeignKey(User)
    plan = models.ForeignKey(Plan)
    amount = models.DecimalField(max_digits=5, decimal_places=2)
    time_created = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return '%s %s' % (self.user.get_full_name(), self.plan.name)

class Return(models.Model):
    investment = models.ForeignKey(Investment)
    amount = models.DecimalField(max_digits=5, decimal_places=2)
    time_created = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return '%s %s' % (self.investment.user.get_full_name(), str(self.amount))
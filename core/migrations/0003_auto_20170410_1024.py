# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-10 10:24
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20170407_1255'),
    ]

    operations = [
        migrations.RenameField(
            model_name='plan',
            old_name='min_deposit',
            new_name='deposit',
        ),
    ]

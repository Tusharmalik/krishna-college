# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-25 20:49
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userprofile',
            old_name='User',
            new_name='user',
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-21 21:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_auto_20170622_0236'),
    ]

    operations = [
        migrations.AlterField(
            model_name='slideshow',
            name='upload',
            field=models.ImageField(upload_to='static/img/buildings'),
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-12-02 10:54
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('tg_app', '0011_auto_20171202_1053'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='posted_on',
            field=models.DateTimeField(default=datetime.datetime(2017, 12, 2, 10, 54, 24, 435704, tzinfo=utc)),
        ),
    ]

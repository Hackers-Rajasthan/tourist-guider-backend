# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-12-02 11:03
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('tg_app', '0014_auto_20171202_1058'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='posted_on',
            field=models.DateTimeField(default=datetime.datetime(2017, 12, 2, 11, 3, 21, 824738, tzinfo=utc)),
        ),
    ]

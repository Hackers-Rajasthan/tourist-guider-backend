# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-12-02 11:44
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('tg_app', '0015_auto_20171202_1103'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='about',
        ),
        migrations.RemoveField(
            model_name='customer',
            name='name',
        ),
        migrations.AlterField(
            model_name='event',
            name='posted_on',
            field=models.DateTimeField(default=datetime.datetime(2017, 12, 2, 11, 44, 35, 232747, tzinfo=utc)),
        ),
    ]
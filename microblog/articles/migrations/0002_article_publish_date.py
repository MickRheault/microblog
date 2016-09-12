# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-06 20:40
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='publish_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2016, 9, 6, 20, 40, 11, 454539, tzinfo=utc)),
            preserve_default=False,
        ),
    ]

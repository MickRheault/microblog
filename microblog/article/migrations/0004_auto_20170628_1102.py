# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-06-28 11:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0003_auto_20170628_1052'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='to_publish',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Kiedy opublikować'),
        ),
        migrations.AlterIndexTogether(
            name='article',
            index_together=set([('status', 'to_publish'), ('status', 'publish_date')]),
        ),
    ]

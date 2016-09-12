# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-12 17:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tags', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tag',
            name='slug',
            field=models.CharField(max_length=50, unique=True, verbose_name='Slug'),
        ),
        migrations.AlterField(
            model_name='tag',
            name='title',
            field=models.CharField(max_length=50, unique=True, verbose_name='Title'),
        ),
    ]

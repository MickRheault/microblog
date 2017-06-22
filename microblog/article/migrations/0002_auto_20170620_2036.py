# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-06-20 20:36
from __future__ import unicode_literals

from django.db import migrations
import django_fsm


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='publish',
        ),
        migrations.AddField(
            model_name='article',
            name='status',
            field=django_fsm.FSMIntegerField(choices=[(0, 'Draft'), (1, 'Accepted'), (2, 'Published'), (3, 'Hidden')], default=0, protected=True),
        ),
    ]
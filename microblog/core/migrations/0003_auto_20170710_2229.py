# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-10 22:29
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_lniks'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Lniks',
            new_name='Link',
        ),
    ]
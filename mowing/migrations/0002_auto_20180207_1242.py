# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-02-07 12:42
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mowing', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='mowing',
            old_name='date',
            new_name='mow_date',
        ),
    ]

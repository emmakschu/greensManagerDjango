# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-02-28 19:24
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('parts', '0003_auto_20180207_1214'),
    ]

    operations = [
        migrations.RenameField(
            model_name='fluid',
            old_name='last_updated',
            new_name='updated_at',
        ),
        migrations.RenameField(
            model_name='part',
            old_name='date_added',
            new_name='created_at',
        ),
        migrations.RenameField(
            model_name='part',
            old_name='last_updated',
            new_name='updated_at',
        ),
        migrations.AddField(
            model_name='fluid',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-02-28 22:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('machines', '0009_auto_20180228_1324'),
        ('fertilizing', '0006_auto_20180228_1324'),
    ]

    operations = [
        migrations.AddField(
            model_name='fertilizer',
            name='spreader',
            field=models.ManyToManyField(to='machines.FertSpreader'),
        ),
    ]
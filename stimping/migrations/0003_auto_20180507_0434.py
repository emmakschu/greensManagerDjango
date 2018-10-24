# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-05-07 09:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stimping', '0002_auto_20180507_0422'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stimp',
            name='backwardAvg',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='stimp',
            name='forwardAvg',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='stimp',
            name='leftAvg',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='stimp',
            name='rightAvg',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
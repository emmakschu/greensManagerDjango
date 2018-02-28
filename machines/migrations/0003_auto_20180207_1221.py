# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-02-07 12:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('machines', '0002_auto_20180207_1219'),
    ]

    operations = [
        migrations.AlterField(
            model_name='machine',
            name='fuel_filter',
            field=models.ManyToManyField(blank=True, null=True, related_name='_machine_fuel_filter_+', to='parts.Filter'),
        ),
        migrations.AlterField(
            model_name='machine',
            name='fuel_type',
            field=models.ManyToManyField(blank=True, null=True, related_name='_machine_fuel_type_+', to='parts.Fuel'),
        ),
        migrations.AlterField(
            model_name='machine',
            name='hyd_oil_filter',
            field=models.ManyToManyField(blank=True, null=True, related_name='_machine_hyd_oil_filter_+', to='parts.Filter'),
        ),
        migrations.AlterField(
            model_name='machine',
            name='hyd_oil_type',
            field=models.ManyToManyField(blank=True, null=True, related_name='_machine_hyd_oil_type_+', to='parts.Oil'),
        ),
        migrations.AlterField(
            model_name='machine',
            name='oil_filter',
            field=models.ManyToManyField(blank=True, null=True, related_name='_machine_oil_filter_+', to='parts.Filter'),
        ),
        migrations.AlterField(
            model_name='machine',
            name='oil_type',
            field=models.ManyToManyField(blank=True, null=True, related_name='_machine_oil_type_+', to='parts.Oil'),
        ),
        migrations.AlterField(
            model_name='roller',
            name='roll_width',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='utilvehicle',
            name='bed_size',
            field=models.FloatField(blank=True, null=True),
        ),
    ]

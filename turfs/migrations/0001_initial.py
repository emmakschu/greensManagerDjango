# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-02-06 20:07
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cultivar',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
            ],
        ),
        migrations.CreateModel(
            name='SoilType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('sand_ratio', models.FloatField()),
                ('silt_ratio', models.FloatField()),
                ('clay_ratio', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='TurfgrassGenus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('common_name', models.CharField(max_length=256)),
            ],
        ),
        migrations.CreateModel(
            name='TurfgrassSpecies',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('common_name', models.CharField(max_length=256)),
                ('genus', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='turfs.TurfgrassGenus')),
            ],
        ),
        migrations.AddField(
            model_name='cultivar',
            name='species',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='turfs.TurfgrassSpecies'),
        ),
    ]

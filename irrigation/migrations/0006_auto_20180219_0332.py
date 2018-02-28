# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-02-19 03:32
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0002_auto_20180206_2046'),
        ('irrigation', '0005_auto_20180207_1214'),
    ]

    operations = [
        migrations.CreateModel(
            name='ShutoffValve',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.BooleanField()),
                ('latitude', models.FloatField()),
                ('longitude', models.FloatField()),
                ('problem', models.BooleanField(default=False)),
                ('fairway', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='courses.Fairway')),
                ('green', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='courses.Green')),
                ('rough', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='courses.Rough')),
                ('tee', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='courses.Tee')),
            ],
        ),
        migrations.AddField(
            model_name='drain',
            name='problem',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='irrigationdig',
            name='fixed',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='quickcoupler',
            name='problem',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='satellitebox',
            name='problem',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='sprinklerhead',
            name='problem',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='drain',
            name='status',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='irrigationdig',
            name='sprinkler',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='irrigation.SprinklerHead'),
        ),
    ]

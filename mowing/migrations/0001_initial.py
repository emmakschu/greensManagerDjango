# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-02-07 12:17
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('courses', '0002_auto_20180206_2046'),
        ('machines', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Mowing',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='FairwayMowing',
            fields=[
                ('mowing_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='mowing.Mowing')),
                ('fairway', models.ManyToManyField(to='courses.Fairway')),
                ('mower', models.ManyToManyField(to='machines.FairwayMower')),
            ],
            bases=('mowing.mowing',),
        ),
        migrations.CreateModel(
            name='GreensMowing',
            fields=[
                ('mowing_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='mowing.Mowing')),
                ('green', models.ManyToManyField(to='courses.Green')),
                ('mower', models.ManyToManyField(to='machines.GreensMower')),
            ],
            bases=('mowing.mowing',),
        ),
        migrations.CreateModel(
            name='RoughMowing',
            fields=[
                ('mowing_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='mowing.Mowing')),
                ('mower', models.ManyToManyField(to='machines.RoughMower')),
                ('rough', models.ManyToManyField(to='courses.Rough')),
            ],
            bases=('mowing.mowing',),
        ),
        migrations.CreateModel(
            name='TeeMowing',
            fields=[
                ('mowing_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='mowing.Mowing')),
                ('mower', models.ManyToManyField(to='machines.TeeMower')),
                ('tee', models.ManyToManyField(to='courses.Tee')),
            ],
            bases=('mowing.mowing',),
        ),
    ]

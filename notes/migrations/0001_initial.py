# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Note',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('content', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='DailyNote',
            fields=[
                ('note_ptr', models.OneToOneField(primary_key=True, auto_created=True, serialize=False, to='notes.Note', parent_link=True)),
                ('valid_date', models.DateField()),
            ],
            bases=('notes.note',),
        ),
        migrations.CreateModel(
            name='WeeklyNote',
            fields=[
                ('note_ptr', models.OneToOneField(primary_key=True, auto_created=True, serialize=False, to='notes.Note', parent_link=True)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
            ],
            bases=('notes.note',),
        ),
        migrations.AddField(
            model_name='note',
            name='created_by',
            field=models.ForeignKey(related_name='creator', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='note',
            name='updated_by',
            field=models.ForeignKey(related_name='editor', to=settings.AUTH_USER_MODEL),
        ),
    ]

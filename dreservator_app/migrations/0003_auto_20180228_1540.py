# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-02-28 14:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dreservator_app', '0002_auto_20180228_1100'),
    ]

    operations = [
        migrations.AddField(
            model_name='reservations',
            name='activities_type',
            field=models.IntegerField(choices=[(1, 'Lekcja'), (2, 'Ćwiczenia')], default=2, verbose_name='Rodzaj zajęć'),
        ),
        migrations.AlterField(
            model_name='users',
            name='first_time',
            field=models.BooleanField(default=True, verbose_name='Nowo zarejestrowany'),
        ),
    ]

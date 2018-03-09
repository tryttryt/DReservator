# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-02-28 15:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dreservator_app', '0003_auto_20180228_1540'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservations',
            name='activities_type',
            field=models.CharField(choices=[('Lekcja', 'Lekcja'), ('Ćwiczenia', 'Ćwiczenia')], default='Ćwiczenia', max_length=15, verbose_name='Rodzaj zajęć'),
        ),
    ]
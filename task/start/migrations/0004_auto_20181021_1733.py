# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-10-21 17:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('start', '0003_auto_20181021_1727'),
    ]

    operations = [
        migrations.AlterField(
            model_name='branch',
            name='address',
            field=models.CharField(max_length=100, verbose_name='Адрес'),
        ),
        migrations.AlterField(
            model_name='branch',
            name='latitude',
            field=models.CharField(max_length=100, verbose_name='Широта'),
        ),
        migrations.AlterField(
            model_name='branch',
            name='longitude',
            field=models.CharField(max_length=100, verbose_name='Долгота'),
        ),
    ]

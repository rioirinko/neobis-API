# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-10-23 21:40
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Branch',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=100, verbose_name='Адрес')),
                ('latitude', models.CharField(max_length=100, verbose_name='Широта')),
                ('longitude', models.CharField(max_length=100, verbose_name='Долгота')),
            ],
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.IntegerField(choices=[(1, 'PHONE'), (2, 'FACEBOOK'), (3, 'EMAIL')], default=1)),
                ('value', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Courses',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Название')),
                ('description', models.CharField(max_length=100, verbose_name='Описание')),
                ('category', models.CharField(max_length=100, verbose_name='Категория')),
                ('logo', models.CharField(max_length=100, verbose_name='Логотип')),
            ],
            options={
                'verbose_name': 'Курс',
                'verbose_name_plural': 'Курсы',
            },
        ),
        migrations.AddField(
            model_name='contact',
            name='courses',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='contacts', to='start.Courses'),
        ),
        migrations.AddField(
            model_name='branch',
            name='courses',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='branches', to='start.Courses'),
        ),
    ]

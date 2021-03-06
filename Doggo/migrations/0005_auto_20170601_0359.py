# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-06-01 01:59
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('Doggo', '0004_auto_20170531_1913'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='wybory',
            name='czasWyboru',
        ),
        migrations.AddField(
            model_name='wybory',
            name='end_time',
            field=models.DateField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='wybory',
            name='start_time',
            field=models.DateField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='glosujacy',
            name='pesel',
            field=models.BigIntegerField(unique=True),
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-31 14:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20170831_1411'),
    ]

    operations = [
        migrations.AlterField(
            model_name='picface',
            name='is_deleted',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='picture',
            name='is_deleted',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='picture',
            name='is_detected',
            field=models.BooleanField(default=False),
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-01 01:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_auto_20170831_1633'),
    ]

    operations = [
        migrations.AddField(
            model_name='face',
            name='s_picname',
            field=models.CharField(default='', max_length=150),
        ),
        migrations.AlterField(
            model_name='face',
            name='face_info',
            field=models.CharField(default='', max_length=150),
        ),
    ]

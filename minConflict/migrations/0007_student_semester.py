# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-02-27 21:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('minConflict', '0006_auto_20180225_1905'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='semester',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-02-28 01:04
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('minConflict', '0015_auto_20180227_1947'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student',
            old_name='year',
            new_name='class_year',
        ),
    ]

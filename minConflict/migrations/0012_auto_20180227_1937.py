# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-02-28 00:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('minConflict', '0011_auto_20180227_1921'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='student_id',
            field=models.IntegerField(unique=True),
        ),
    ]

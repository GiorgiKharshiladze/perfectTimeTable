# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-02-27 22:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('minConflict', '0007_student_semester'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='semester',
            field=models.CharField(max_length=100),
        ),
    ]

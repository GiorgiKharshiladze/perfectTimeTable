# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-02-26 00:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('minConflict', '0003_student'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='final_schedule',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='course',
            name='num_enrolled',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='final_courses',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='major',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='student',
            name='preferred_courses',
            field=models.TextField(blank=True),
        ),
    ]

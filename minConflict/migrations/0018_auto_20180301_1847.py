# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-03-01 23:47
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('minConflict', '0017_auto_20180227_2011'),
    ]

    operations = [
        migrations.RenameField(
            model_name='course',
            old_name='crn',
            new_name='cnr',
        ),
    ]

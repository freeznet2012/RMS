# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-18 08:13
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('retest', '0008_auto_20170313_1407'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='retest',
            name='semester',
        ),
        migrations.RemoveField(
            model_name='student',
            name='sem',
        ),
        migrations.RemoveField(
            model_name='subject',
            name='semester',
        ),
        migrations.DeleteModel(
            name='Semester',
        ),
    ]

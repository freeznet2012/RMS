# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-13 08:37
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('retest', '0007_remove_semester_batch'),
    ]

    operations = [
        migrations.RenameField(
            model_name='subject',
            old_name='subject',
            new_name='sub',
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-30 11:59
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('retest', '0051_remove_projectors_available'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='auditoriums',
            name='head',
        ),
        migrations.RemoveField(
            model_name='classroom',
            name='head',
        ),
        migrations.RemoveField(
            model_name='extension_cables',
            name='sec',
        ),
        migrations.RemoveField(
            model_name='graphicshalls',
            name='head',
        ),
        migrations.RemoveField(
            model_name='labs',
            name='sec',
        ),
        migrations.RemoveField(
            model_name='mikesystems',
            name='head',
        ),
        migrations.RemoveField(
            model_name='projectors',
            name='sec',
        ),
    ]
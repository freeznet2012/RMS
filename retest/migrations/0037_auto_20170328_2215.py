# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-28 16:45
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('admin', '0002_logentry_remove_auto_add'),
        ('retest', '0036_customusers'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customusers',
            name='user_ptr',
        ),
        migrations.AlterField(
            model_name='customuser',
            name='dept',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='retest.Departement'),
        ),
        migrations.DeleteModel(
            name='CustomUsers',
        ),
    ]
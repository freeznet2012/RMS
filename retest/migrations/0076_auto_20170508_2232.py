# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-05-08 17:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('retest', '0075_auto_20170508_2008'),
    ]

    operations = [
        migrations.AddField(
            model_name='eventauditorium',
            name='recieved',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='eventclassroom',
            name='recieved',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='eventgraphicshall',
            name='recieved',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='eventlab',
            name='recieved',
            field=models.BooleanField(default=False),
        ),
    ]

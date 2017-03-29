# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-24 18:15
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('retest', '0017_auto_20170318_1542'),
    ]

    operations = [
        migrations.CreateModel(
            name='Accepted',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(blank=True, null=True)),
                ('name', models.CharField(max_length=50)),
                ('reason', models.CharField(max_length=50)),
                ('proof', models.CharField(max_length=200)),
                ('admnno', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='retest.Student')),
                ('batch', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='retest.Batch')),
                ('dept', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='retest.Departement')),
                ('semester', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='retest.Semester')),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='retest.Subject')),
            ],
        ),
    ]

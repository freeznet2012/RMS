# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-29 21:40
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('retest', '0044_auto_20170430_0302'),
    ]

    operations = [
        migrations.CreateModel(
            name='Auditoriums',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('audi', models.CharField(max_length=50)),
                ('head', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Classroom',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('roomno', models.CharField(max_length=50)),
                ('head', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Eventauditorium',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(blank=True, null=True)),
                ('fromt', models.CharField(max_length=50, null=True)),
                ('to', models.CharField(max_length=50, null=True)),
                ('is_accept', models.IntegerField(default=0)),
                ('auditorium', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='retest.Auditoriums')),
            ],
        ),
        migrations.CreateModel(
            name='Eventclassroom',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(blank=True, null=True)),
                ('fromt', models.CharField(max_length=50, null=True)),
                ('to', models.CharField(max_length=50, null=True)),
                ('is_accept', models.IntegerField(default=0)),
                ('classroom', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='retest.Classroom')),
            ],
        ),
        migrations.CreateModel(
            name='Eventextensioncable',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(blank=True, null=True)),
                ('fromt', models.CharField(max_length=50, null=True)),
                ('to', models.CharField(max_length=50, null=True)),
                ('is_accept', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Eventgraphicshall',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(blank=True, null=True)),
                ('fromt', models.CharField(max_length=50, null=True)),
                ('to', models.CharField(max_length=50, null=True)),
                ('is_incharge', models.BooleanField(default=False)),
                ('is_ashok', models.BooleanField(default=False)),
                ('is_principal', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Eventlab',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(blank=True, null=True)),
                ('fromt', models.CharField(max_length=50, null=True)),
                ('to', models.CharField(max_length=50, null=True)),
                ('is_accept', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Eventmikesystem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(blank=True, null=True)),
                ('fromt', models.CharField(max_length=50, null=True)),
                ('to', models.CharField(max_length=50, null=True)),
                ('is_accept', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Eventprojector',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(blank=True, null=True)),
                ('fromt', models.CharField(max_length=50, null=True)),
                ('to', models.CharField(max_length=50, null=True)),
                ('is_accept', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Extension_cables',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cable', models.CharField(max_length=50)),
                ('sec', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='retest.Section')),
            ],
        ),
        migrations.CreateModel(
            name='Graphicshalls',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('graph', models.CharField(max_length=50)),
                ('head', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Labs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('sec', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='retest.Section')),
            ],
        ),
        migrations.CreateModel(
            name='Mikesystems',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mike', models.CharField(max_length=50)),
                ('head', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Projectors',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pro', models.CharField(max_length=50)),
                ('sec', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='retest.Section')),
            ],
        ),
        migrations.AddField(
            model_name='eventprojector',
            name='projector',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='retest.Projectors'),
        ),
        migrations.AddField(
            model_name='eventmikesystem',
            name='mike_system',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='retest.Mikesystems'),
        ),
        migrations.AddField(
            model_name='eventlab',
            name='lab',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='retest.Labs'),
        ),
        migrations.AddField(
            model_name='eventgraphicshall',
            name='graphics_hall',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='retest.Graphicshalls'),
        ),
        migrations.AddField(
            model_name='eventextensioncable',
            name='extension_cable',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='retest.Extension_cables'),
        ),
    ]

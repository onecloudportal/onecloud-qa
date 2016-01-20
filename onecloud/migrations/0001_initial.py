# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-14 11:49
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Provider',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80)),
                ('cpu', models.PositiveIntegerField()),
                ('memory', models.PositiveIntegerField(help_text=b'Memory(Ram) in GB')),
                ('disk', models.PositiveIntegerField(help_text=b'Disk size in GB')),
                ('price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('provider', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='services', to='onecloud.Provider')),
            ],
            options={
                'ordering': ['price'],
            },
        ),
    ]
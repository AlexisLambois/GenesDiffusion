# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-19 10:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('form', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('mdp', models.CharField(max_length=20)),
                ('droit_insertion', models.NullBooleanField()),
            ],
        ),
    ]

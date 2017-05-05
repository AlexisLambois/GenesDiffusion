# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-05 07:11
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('form', '0007_auto_20170425_1001'),
    ]

    operations = [
        migrations.RenameField(
            model_name='preleveur',
            old_name='numeroagrement',
            new_name='numero',
        ),
        migrations.AddField(
            model_name='prelevement',
            name='preleveur',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='form.Preleveur'),
            preserve_default=False,
        ),
    ]

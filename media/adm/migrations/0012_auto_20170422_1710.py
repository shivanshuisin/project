# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-22 17:10
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('adm', '0011_auto_20170421_0018'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='username',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='adm.User'),
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-12 17:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adm', '0006_auto_20170411_1407'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='current_month',
            field=models.FileField(upload_to=b''),
        ),
        migrations.AlterField(
            model_name='user',
            name='oldest_month',
            field=models.FileField(upload_to=b''),
        ),
        migrations.AlterField(
            model_name='user',
            name='previous_month',
            field=models.FileField(upload_to=b''),
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-04 21:25
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('adm', '0002_auto_20170404_1943'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='depatment',
            new_name='department',
        ),
    ]

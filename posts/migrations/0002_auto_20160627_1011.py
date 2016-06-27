# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-27 10:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posts',
            name='date_add',
            field=models.DateTimeField(auto_now=True, verbose_name='Date added'),
        ),
        migrations.AlterField(
            model_name='posts',
            name='date_pub',
            field=models.DateTimeField(null=True, verbose_name='Date published'),
        ),
    ]

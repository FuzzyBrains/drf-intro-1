# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-10-02 10:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='talk',
            name='topic',
            field=models.CharField(max_length=200, unique=True),
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-05-12 11:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('samples', '0006_auto_20180512_1124'),
    ]

    operations = [
        migrations.AlterField(
            model_name='explosamplefile',
            name='handledUrl',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='处理完的文件'),
        ),
    ]

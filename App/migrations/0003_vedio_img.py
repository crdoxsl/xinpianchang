# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-12-17 10:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0002_vedio'),
    ]

    operations = [
        migrations.AddField(
            model_name='vedio',
            name='img',
            field=models.CharField(default='1', max_length=200),
            preserve_default=False,
        ),
    ]

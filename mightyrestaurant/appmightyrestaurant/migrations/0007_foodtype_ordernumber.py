# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-08 15:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appmightyrestaurant', '0006_auto_20160708_1338'),
    ]

    operations = [
        migrations.AddField(
            model_name='foodtype',
            name='ordernumber',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]

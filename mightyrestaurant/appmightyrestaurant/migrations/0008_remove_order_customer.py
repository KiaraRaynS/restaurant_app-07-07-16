# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-08 19:06
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appmightyrestaurant', '0007_foodtype_ordernumber'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='customer',
        ),
    ]

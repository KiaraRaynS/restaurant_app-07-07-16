# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-07 18:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appmightyrestaurant', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='notes',
            field=models.TextField(blank=True, null=True),
        ),
    ]

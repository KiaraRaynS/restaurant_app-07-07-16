# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-08 13:38
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('appmightyrestaurant', '0005_auto_20160708_0939'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomerTable',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('partyname', models.CharField(max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='order',
            name='tableid',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='appmightyrestaurant.CustomerTable'),
            preserve_default=False,
        ),
    ]

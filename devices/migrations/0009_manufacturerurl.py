# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-10-15 08:31
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('devices', '0008_auto_20180924_1512'),
    ]

    operations = [
        migrations.CreateModel(
            name='ManufacturerUrl',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Name')),
                ('url', models.CharField(max_length=200, verbose_name='Url')),
                ('manufacturer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='urls', to='devices.Manufacturer')),
            ],
            options={
                'permissions': (('read_url', 'Can read Url'),),
            },
        ),
    ]

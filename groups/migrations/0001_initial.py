# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2019-04-08 07:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Groups',
            fields=[
                ('pk_bint_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('vchr_code', models.CharField(blank=True, max_length=50, null=True)),
                ('vchr_name', models.CharField(blank=True, max_length=150, null=True)),
                ('int_status', models.IntegerField(blank=True, default=1, null=True)),
            ],
            options={
                'managed': False,
                'db_table': 'groups',
            },
        ),
    ]

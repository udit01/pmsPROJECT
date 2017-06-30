# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-30 20:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('oAuth', '0002_userprofile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='type',
            field=models.CharField(choices=[('AD', 'Admin'), ('CL', 'Client')], default='CL', max_length=2),
        ),
    ]

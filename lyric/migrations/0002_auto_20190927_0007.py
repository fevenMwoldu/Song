# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2019-09-26 21:07
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lyric', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Mezmur',
            new_name='Song',
        ),
        migrations.RenameField(
            model_name='song',
            old_name='lyrics',
            new_name='lyric',
        ),
    ]

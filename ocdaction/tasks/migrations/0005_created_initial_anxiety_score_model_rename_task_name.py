# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2017-02-05 13:58
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0004_created_initial_anxiety_score_model'),
    ]

    operations = [
        migrations.RenameField(
            model_name='task',
            old_name='taskname',
            new_name='task_name',
        ),
    ]

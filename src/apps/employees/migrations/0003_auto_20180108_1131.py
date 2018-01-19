# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-01-08 08:28
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion



class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('employees', '0002_auto_20180108_1128'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employee',
            name='additional_phone_number',
        ),
        migrations.RemoveField(
            model_name='employee',
            name='contact_email',
        ),
        migrations.RemoveField(
            model_name='employee',
            name='phone_number',
        ),
        migrations.AddField(
            model_name='employee',
            name='user',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='employee', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
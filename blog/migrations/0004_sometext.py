# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-10-27 17:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_remove_post_preview'),
    ]

    operations = [
        migrations.CreateModel(
            name='SomeText',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
            ],
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-29 19:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('categories', '0002_remove_category_posts'),
        ('posts', '0002_post_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='categories',
            field=models.ManyToManyField(to='categories.Category'),
        ),
    ]

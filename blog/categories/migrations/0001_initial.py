# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-29 18:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('posts', '0002_post_author'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('posts', models.ManyToManyField(to='posts.Post')),
            ],
        ),
    ]

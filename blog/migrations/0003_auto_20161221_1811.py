# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-12-21 12:41
from __future__ import unicode_literals

from django.db import migrations, models
import django_markdown.models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.CharField(max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='text',
            field=django_markdown.models.MarkdownField(),
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2018-04-12 03:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('general', '0015_auto_20170614_2038'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sister',
            name='profile_image',
            field=models.ImageField(blank=True, default='images/default.png', height_field='image_height', null=True, upload_to='images', width_field='image_width'),
        ),
    ]

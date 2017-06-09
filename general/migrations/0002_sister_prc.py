# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-09 19:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('general', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='sister',
            name='prc',
            field=models.CharField(choices=[('Y', 'PRC'), ('N', 'Non-PRC')], default='N', max_length=1),
        ),
    ]
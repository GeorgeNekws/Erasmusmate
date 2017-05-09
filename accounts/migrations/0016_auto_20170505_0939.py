# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-05 09:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0015_auto_20170505_0938'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='men_or_women_on_room',
            field=models.CharField(choices=[("Don't care", "Don't care"), ('Men only', 'Men only'), ('Women only', 'Women only')], default='', max_length=20),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='prefered_cuisine',
            field=models.CharField(choices=[('GR', 'GREEK'), ('FR', 'FRENCH'), ('CHINESE', 'CHINESE'), ('INTERNATIONAL', 'INTERNATIONAL')], default='', max_length=10),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='same_nationality_roommates',
            field=models.CharField(choices=[("Don't care", "Don't care"), ('Yes', 'Yes'), ('No', 'No')], default='', max_length=10),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='smoker',
            field=models.CharField(choices=[("Don't care", "Don't care"), ('Yes', 'Yes'), ('No', 'No')], default='', max_length=10),
        ),
    ]
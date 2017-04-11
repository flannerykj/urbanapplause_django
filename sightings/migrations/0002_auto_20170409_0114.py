# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-09 01:14
from __future__ import unicode_literals

from django.db import migrations
import geoposition.fields


class Migration(migrations.Migration):

    dependencies = [
        ('sightings', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sighting',
            name='location',
            field=geoposition.fields.GeopositionField(max_length=42),
        ),
    ]
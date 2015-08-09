# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django_extensions.db.fields.json


class Migration(migrations.Migration):

    dependencies = [
        ('income', '0010_auto_20150808_2120'),
    ]

    operations = [
        migrations.AddField(
            model_name='incometarget',
            name='coeffs',
            field=django_extensions.db.fields.json.JSONField(default='[]'),
        ),
    ]

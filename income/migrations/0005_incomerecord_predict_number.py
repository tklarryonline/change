# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('income', '0004_auto_20150808_0412'),
    ]

    operations = [
        migrations.AddField(
            model_name='incomerecord',
            name='predict_number',
            field=models.FloatField(default=0, verbose_name='Predicted Income'),
        ),
    ]

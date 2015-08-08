# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('income', '0009_auto_20150808_2056'),
    ]

    operations = [
        migrations.AlterField(
            model_name='incometarget',
            name='month',
            field=models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10), (11, 11), (12, 12)], default=1),
        ),
        migrations.AlterField(
            model_name='incometarget',
            name='number',
            field=models.FloatField(verbose_name='Income', default=0),
        ),
        migrations.AlterField(
            model_name='incometarget',
            name='year',
            field=models.IntegerField(default=0),
        ),
    ]

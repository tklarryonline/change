# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('income', '0006_incomepredict'),
    ]

    operations = [
        migrations.AlterField(
            model_name='incomepredict',
            name='number',
            field=models.FloatField(default=0, verbose_name='Income'),
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('change', '0003_auto_20150808_0409'),
    ]

    operations = [
        migrations.AlterField(
            model_name='incomerecord',
            name='number',
            field=models.FloatField(verbose_name='Income'),
        ),
    ]

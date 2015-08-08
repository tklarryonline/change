# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('change', '0002_auto_20150808_0407'),
    ]

    operations = [
        migrations.RenameField(
            model_name='IncomeRecord',
            old_name='user_id',
            new_name='user'
        ),
    ]

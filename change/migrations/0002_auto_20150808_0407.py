# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('change', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Record',
            new_name='IncomeRecord',
        )
    ]

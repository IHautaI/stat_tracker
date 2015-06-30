# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stats', '0002_auto_20150629_1901'),
    ]

    operations = [
        migrations.RenameField(
            model_name='entry',
            old_name='timestamp',
            new_name='date',
        ),
        migrations.AddField(
            model_name='entry',
            name='count',
            field=models.IntegerField(default=0),
        ),
    ]

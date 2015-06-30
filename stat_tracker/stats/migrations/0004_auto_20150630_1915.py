# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stats', '0003_auto_20150630_1909'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entry',
            name='activity',
            field=models.ForeignKey(null=True, to='stats.Activity', related_name='stats'),
        ),
    ]

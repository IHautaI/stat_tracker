# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
        ('stats', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='activity',
            name='profile',
            field=models.ForeignKey(to='users.Profile', null=True),
        ),
        migrations.AddField(
            model_name='entry',
            name='activity',
            field=models.ForeignKey(to='stats.Activity', null=True),
        ),
        migrations.AlterField(
            model_name='entry',
            name='timestamp',
            field=models.DateField(),
        ),
    ]

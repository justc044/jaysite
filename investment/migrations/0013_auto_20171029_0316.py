# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('investment', '0012_auto_20171029_0315'),
    ]

    operations = [
        migrations.AddField(
            model_name='goals',
            name='goal_date',
            field=models.DateTimeField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='blog',
            name='post_date',
            field=models.DateTimeField(default=datetime.datetime(2017, 10, 29, 3, 16, 11, 511250)),
        ),
        migrations.AlterField(
            model_name='goals',
            name='post_date',
            field=models.DateTimeField(default=datetime.datetime(2017, 10, 29, 3, 16, 11, 510795)),
        ),
    ]

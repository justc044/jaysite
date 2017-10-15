# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('investment', '0004_auto_20171008_0712'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='stockmarketitem',
            name='comment',
        ),
        migrations.AddField(
            model_name='stockmarketitem',
            name='comment_after',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='stockmarketitem',
            name='comment_before',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='stockmarketitem',
            name='comment_during',
            field=models.TextField(blank=True),
        ),
    ]

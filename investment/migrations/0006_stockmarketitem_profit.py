# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('investment', '0005_auto_20171008_0719'),
    ]

    operations = [
        migrations.AddField(
            model_name='stockmarketitem',
            name='profit',
            field=models.PositiveIntegerField(null=True, blank=True),
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('investment', '0002_auto_20171008_0707'),
    ]

    operations = [
        migrations.AlterField(
            model_name='phase',
            name='enddate',
            field=models.DateTimeField(null=True),
        ),
    ]

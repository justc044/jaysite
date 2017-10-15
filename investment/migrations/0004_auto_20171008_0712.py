# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('investment', '0003_auto_20171008_0711'),
    ]

    operations = [
        migrations.AlterField(
            model_name='phase',
            name='enddate',
            field=models.DateTimeField(null=True, blank=True),
        ),
    ]

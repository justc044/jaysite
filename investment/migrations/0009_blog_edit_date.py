# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('investment', '0008_auto_20171015_0442'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='edit_date',
            field=models.DateTimeField(null=True, blank=True),
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('investment', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='realestateitem',
            name='investment_segment',
            field=models.OneToOneField(to='investment.RESegment'),
        ),
        migrations.AlterField(
            model_name='realestateitem',
            name='phase',
            field=models.OneToOneField(to='investment.Phase'),
        ),
        migrations.AlterField(
            model_name='stockmarketitem',
            name='investment_segment',
            field=models.OneToOneField(to='investment.SMSegment'),
        ),
        migrations.AlterField(
            model_name='stockmarketitem',
            name='phase',
            field=models.OneToOneField(to='investment.Phase'),
        ),
    ]

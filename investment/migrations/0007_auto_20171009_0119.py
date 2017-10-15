# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('investment', '0006_stockmarketitem_profit'),
    ]

    operations = [
        migrations.AlterField(
            model_name='realestateitem',
            name='investment_segment',
            field=models.ForeignKey(to='investment.RESegment'),
        ),
        migrations.AlterField(
            model_name='realestateitem',
            name='phase',
            field=models.ForeignKey(to='investment.Phase'),
        ),
        migrations.AlterField(
            model_name='stockmarketitem',
            name='investment_segment',
            field=models.ForeignKey(to='investment.SMSegment'),
        ),
        migrations.AlterField(
            model_name='stockmarketitem',
            name='phase',
            field=models.ForeignKey(to='investment.Phase'),
        ),
    ]

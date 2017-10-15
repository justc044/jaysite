# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Objective',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('text', models.CharField(max_length=400)),
                ('post_date', models.DateTimeField(null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Phase',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('startdate', models.DateTimeField()),
                ('enddate', models.DateTimeField()),
                ('no', models.PositiveSmallIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='RealEstateItem',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('portion', models.DecimalField(max_digits=3, decimal_places=0)),
                ('description', models.CharField(max_length=450)),
                ('comment', models.TextField()),
                ('chosen', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='RESegment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('segment_type', models.CharField(default=b'AP', max_length=2, choices=[(b'AP', b'Apartment'), (b'OF', b'Officetel')])),
            ],
        ),
        migrations.CreateModel(
            name='SMSegment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('segment_country', models.CharField(default=b'KOR', max_length=3, choices=[(b'KOR', b'Korea'), (b'USA', b'United States'), (b'EUR', b'Europe'), (b'CHN', b'China')])),
            ],
        ),
        migrations.CreateModel(
            name='StockMarketItem',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('portion', models.DecimalField(max_digits=3, decimal_places=0)),
                ('description', models.CharField(max_length=450)),
                ('comment', models.TextField()),
                ('chosen', models.BooleanField()),
                ('investment_segment', models.ForeignKey(to='investment.SMSegment', unique=True)),
                ('phase', models.ForeignKey(to='investment.Phase', unique=True)),
            ],
        ),
        migrations.AddField(
            model_name='realestateitem',
            name='investment_segment',
            field=models.ForeignKey(to='investment.RESegment', unique=True),
        ),
        migrations.AddField(
            model_name='realestateitem',
            name='phase',
            field=models.ForeignKey(to='investment.Phase', unique=True),
        ),
    ]

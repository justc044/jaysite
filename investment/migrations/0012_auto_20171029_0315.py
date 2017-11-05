# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('investment', '0011_auto_20171015_1356'),
    ]

    operations = [
        migrations.CreateModel(
            name='Goals',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('post_date', models.DateTimeField(default=datetime.datetime(2017, 10, 29, 3, 15, 18, 861103))),
                ('edit_date', models.DateTimeField(null=True, blank=True)),
                ('title', models.CharField(max_length=200)),
                ('text', models.TextField()),
            ],
        ),
        migrations.AlterField(
            model_name='blog',
            name='post_date',
            field=models.DateTimeField(default=datetime.datetime(2017, 10, 29, 3, 15, 18, 861498)),
        ),
    ]

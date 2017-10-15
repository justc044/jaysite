# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('investment', '0010_blog_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='category',
            field=models.CharField(default=b'INVESTMENT', max_length=200, choices=[(b'INVESTMENT', b'\xed\x88\xac\xec\x9e\x90'), (b'COMPANY', b'\xed\x9a\x8c\xec\x82\xac'), (b'HOME', b'\xea\xb0\x80\xec\xa0\x95'), (b'OTHER', b'\xea\xb8\xb0\xed\x83\x80')]),
        ),
        migrations.AlterField(
            model_name='blog',
            name='post_date',
            field=models.DateTimeField(default=datetime.datetime(2017, 10, 15, 13, 56, 32, 990572)),
        ),
    ]

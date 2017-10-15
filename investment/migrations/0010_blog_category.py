# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('investment', '0009_blog_edit_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='category',
            field=models.CharField(default=b'\xed\x88\xac\xec\x9e\x90', max_length=200, choices=[(b'\xed\x88\xac\xec\x9e\x90', b'\xed\x88\xac\xec\x9e\x90'), (b'\xed\x9a\x8c\xec\x82\xac', b'\xed\x9a\x8c\xec\x82\xac'), (b'\xea\xb0\x80\xec\xa0\x95', b'\xea\xb0\x80\xec\xa0\x95'), (b'\xea\xb8\xb0\xed\x83\x80', b'\xea\xb8\xb0\xed\x83\x80')]),
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('investment', '0007_auto_20171009_0119'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('post_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('title', models.CharField(max_length=200)),
                ('text', models.TextField()),
            ],
        ),
        migrations.AlterField(
            model_name='stockmarketitem',
            name='comment_after',
            field=models.TextField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='stockmarketitem',
            name='comment_during',
            field=models.TextField(null=True, blank=True),
        ),
    ]

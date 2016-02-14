# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('yahoo_values', '0002_auto_20160213_0333'),
    ]

    operations = [
        migrations.AlterField(
            model_name='yahoodata',
            name='date',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='yahoodata',
            name='title',
            field=models.CharField(max_length=250),
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('yahoo_values', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='yahoodata',
            old_name='Volume',
            new_name='volume',
        ),
    ]

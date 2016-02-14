# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dynamic_scraper', '0017_added_order_to_scraped_obj_attr'),
    ]

    operations = [
        migrations.CreateModel(
            name='YahooData',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=250, choices=[('Title', ''), ('Date', ''), ('Open', ''), ('close', ''), ('Volume', ''), ('AdjClose', '')])),
                ('date', models.DateTimeField(choices=[('Title', ''), ('Date', ''), ('Open', ''), ('close', ''), ('Volume', ''), ('AdjClose', '')])),
                ('open_at', models.IntegerField()),
                ('close_at', models.IntegerField()),
                ('Volume', models.IntegerField()),
                ('adjusted_close', models.IntegerField()),
                ('checker_runtime', models.ForeignKey(on_delete=django.db.models.deletion.SET_NULL, blank=True, to='dynamic_scraper.SchedulerRuntime', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='YahooWebService',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=250)),
                ('url', models.URLField()),
                ('scraper', models.ForeignKey(on_delete=django.db.models.deletion.SET_NULL, blank=True, to='dynamic_scraper.Scraper', null=True)),
                ('scraper_runtime', models.ForeignKey(on_delete=django.db.models.deletion.SET_NULL, blank=True, to='dynamic_scraper.SchedulerRuntime', null=True)),
            ],
        ),
        migrations.AddField(
            model_name='yahoodata',
            name='yahoo_website',
            field=models.ForeignKey(to='yahoo_values.YahooWebService'),
        ),
    ]

from __future__ import unicode_literals

from django.db import models
from scrapy_djangoitem import DjangoItem
from dynamic_scraper.models import Scraper, SchedulerRuntime

# Create your models here.

class YahooWebService(models.Model):

	title = models.CharField(max_length=250)
	url  = models.URLField()
	scraper = models.ForeignKey(Scraper, blank= True, null=True, on_delete=models.SET_NULL)
	scraper_runtime = models.ForeignKey(SchedulerRuntime, blank= True, null=True, on_delete=models.SET_NULL)

class YahooData(models.Model):
	X_PATH_CHOICES = (
		('Title', ''),
		('Date', ''),
		('Open', ''),
		('close', ''),
		('Volume', ''),
		('AdjClose', ''),
	)

	yahoo_website = models.ForeignKey(YahooWebService)
	checker_runtime = models.ForeignKey(SchedulerRuntime, blank= True, null=True, on_delete=models.SET_NULL)
	title = models.CharField(max_length=250)
	date = models.DateTimeField()
	open_at = models.IntegerField()
	close_at = models.IntegerField()
	volume = models.IntegerField()
	adjusted_close = models.IntegerField()

class YahooDataItem(DjangoItem):

	django_model = YahooData

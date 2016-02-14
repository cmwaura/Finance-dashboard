from __future__ import unicode_literals

from django.contrib import admin
from .models import YahooData, YahooWebService
# Register your models here.

class YahooWebServiceAdmin(admin.ModelAdmin):
	list_display = ('id', 'title', 'url_', 'scraper',)
	list_display_links = ('title',)

	def url_(self, instance):
		return '<a href="{url}" target="_blank">{title}</a>'.format(
			url=instance.url,title=instance.url)

	url_.allow_tags = True

class YahooDataAdmin(admin.ModelAdmin):
	list_display = ('id', 'title', 'date', 'open_at','close_at', 'volume', 'adjusted_close',)
	raw_id_fields = ('checker_runtime',)

	

admin.site.register(YahooWebService, YahooWebServiceAdmin)
admin.site.register(YahooData, YahooDataAdmin)
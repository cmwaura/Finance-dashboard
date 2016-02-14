from __future__ import unicode_literals
from django.db.models.signals import pre_delete
from django.dispatch import receiver
from .models import YahooWebService, YahooData

@receiver(pre_delete)
def pre_delete_handler(sender, instance, using, **kwargs):
	if isinstance(instance, YahooWebService):
		if isinstance.scraper_runtime:
			instance.scraper_runtime.delete()

		if isinstance(instance, YahooData):
			if instance.checker_runtime:
				instance.checker_runtime.delete()

pre_delete.connect(pre_delete_handler)


from django.db import models

from apps.utils.models import Timestamps

class Item(Timestamps, models.Model):
	description = models.CharField(max_length=100)
	serial_number = models.CharField(max_length=100)
	image = models.ImageField(upload_to='item-images')

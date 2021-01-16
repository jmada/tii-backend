from django.db import models

from apps.utils.models import Timestamps

class Model(Timestamps, models.Model):
	name = models.CharField(max_length=100)
	description = models.CharField(max_length=100)

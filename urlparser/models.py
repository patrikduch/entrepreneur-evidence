from django.db import models


class Task(models.Model):
	title = models.CharField(max_length=85, blank=False, unique=True)
	siteName = models.CharField(max_length=85, blank=False, unique=True)
	url = models.CharField(max_length=100, blank=False, unique=True)
	description = models.CharField(max_length=255, blank=True)

	def __str__ (self):
		return self.url



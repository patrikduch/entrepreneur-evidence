from django.db import models


class Task(models.Model):
	title = models.CharField(max_length=85, blank=False)
	siteName = models.CharField(max_length=85, blank=False)
	description = models.CharField(max_length=255, blank=True)

	def __str__ (self):
		return self.siteName



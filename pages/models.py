from django.db import models

class Enterpreneur(models.Model):
	firstName = models.CharField(max_length=255, blank=False)
	lastName = models.CharField(max_length=255, blank=False)
	email = models.EmailField(max_length=255, blank=True)
	ico = models.CharField(max_length=8, blank=False)

	def __str__ (self):
		return self.firstName + ' ' + self.lastName



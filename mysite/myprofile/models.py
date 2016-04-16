from __future__ import unicode_literals

from django.db import models

class MyProfile(models.Model):
	full_name = models.CharField(max_length=100, blank=True)
	bio = models.TextField(blank=True)
	facebook = models.URLField(blank=True)
	github = models.URLField(blank=True)

	def __str__(self):
		return self.full_name;
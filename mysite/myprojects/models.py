from __future__ import unicode_literals

from django.db import models

class MyProject(models.Model):
	title = models.CharField(max_length=100)
	description = models.TextField(blank=True)
	url = models.URLField(blank=True)

	def __str__(self):
		return self.title

class Comment(models.Model):
	project = models.ForeignKey(MyProject, related_name='comments')
	name = models.CharField(max_length=100, default='Anonymous')
	content = models.TextField()

	def __str__(self):
		return self.name + 'said "' + self.content + '"'

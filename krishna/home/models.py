from django.db import models
from django.utils.encoding import python_2_unicode_compatible

@python_2_unicode_compatible
class NoticeBoard(models.Model):
	title = models.CharField(max_length=200)
	pub_date = models.DateTimeField(auto_now=True)
	overview = models.TextField(null=True, blank=True)
	upload = models.FileField(upload_to='static/pdf/notice_board', null=True, blank=True)

	def __str__(self):
		return self.title

@python_2_unicode_compatible
class SlideShow(models.Model):
	title = models.CharField(max_length=100)
	pub_date = models.DateTimeField(auto_now_add=True)
	upload = models.ImageField(upload_to='static/img/buildings')

	def __str__(self):
		return self.title

@python_2_unicode_compatible
class Event(models.Model):
	title = models.CharField(max_length=100)
	pub_date = models.DateTimeField(auto_now=True)
	url = models.URLField(null=True, blank=True)
	upload = models.FileField(upload_to='static/pdf/Event', null=True, blank=True)

	def __str__(self):
		return self.title

@python_2_unicode_compatible
class Highlight(models.Model):
	title = models.CharField(max_length=200)
	pub_date = models.DateTimeField(auto_now=True)
	url = models.URLField(null=True, blank=True)
	upload = models.FileField(upload_to='static/pdf/Highlight', null=True, blank=True)

	def __str__(self):
		return self.title

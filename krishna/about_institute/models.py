from django.db import models
from django.utils.encoding import python_2_unicode_compatible

@python_2_unicode_compatible
class Overview(models.Model):
	heading = models.CharField(max_length=100)
	paragraph = models.TextField()

	def __str__(self):
		return self.heading



@python_2_unicode_compatible
class DirectorsDesk(models.Model):
	director_name = models.CharField(max_length=40)
	director_name_link = models.URLField(null=True, blank=True, help_text="link of the page it should direct too")
	paragraph = models.TextField()
	image = models.ImageField(upload_to='static/img/director')



@python_2_unicode_compatible
class AboutManagement(models.Model):
	heading = models.CharField(max_length=100)
	paragraph = models.TextField()
	chairman_name = models.CharField(max_length=40)
	chairman_position = models.CharField(max_length=60)
	vice_chairman_name = models.CharField(max_length=40)
	vice_chairman_position = models.CharField(max_length=60)
	secretary_name = models.CharField(max_length=40)
	secretary_position = models.CharField(max_length=60)
	treasurer_name = models.CharField(max_length=40)
	treasurer_position = models.CharField(max_length=60)
	advisor_name = models.CharField(max_length=40)
	advisor_position = models.CharField(max_length=60)
	director_name = models.CharField(max_length=40)
	diroctor_position = models.CharField(max_length=60)

	def __str__(self):
		return self.heading



@python_2_unicode_compatible
class ImportantFunctionaries(models.Model):
	Name = models.CharField(max_length=100)
	designation = models.CharField(max_length=100)
	email = models.EmailField()
	contact_no = models.BigIntegerField()



@python_2_unicode_compatible
class VisionAndMission(models.Model):
	vision_text = models.TextField()
	mission_text = models.TextField()



@python_2_unicode_compatible
class Aicte(models.Model):
	title = models.CharField(max_length=50)
	url = models.URLField(null=True, blank=True)
	upload = models.FileField(upload_to='static/pdf/Aicte', null=True, blank=True)

	def __str__(self):
		return self.title

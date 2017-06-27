from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save

class UserProfile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	designation = models.CharField(max_length=100, null=True, blank=True)
	department = models.CharField(max_length=100, null=True, blank=True)
	masters_specialization = models.CharField(max_length=100, null=True, blank=True)
	masters_year = models.IntegerField(null=True, blank=True)
	masters_university = models.CharField(max_length=100, null=True, blank=True)
	btech_specialization = models.CharField(max_length=100, null=True, blank=True)
	btech_year = models.IntegerField(null=True, blank=True)
	btech_university = models.CharField(max_length=100, null=True, blank=True)
	teaching_experience = models.IntegerField(null=True,blank=True,help_text='enter the number only and dont add anything else')
	industry_experience = models.IntegerField(null=True, blank=True,help_text='enter the number only and dont add anything else')
	research_experience = models.IntegerField(null=True, blank=True,help_text='enter the number only and dont add anything else')
	research_interest = models.TextField(null=True, blank=True)
	teaching_interest = models.TextField(null=True, blank=True)
	research_paper_published = models.IntegerField(null=True, blank=True)
	summary = models.TextField(null=True, blank=True, help_text='write a summary about yourself')
	image = models.ImageField(upload_to='static/img/faculty',null=True,blank=True)
	
	def __str__(self):
		return self.user.username

def create_profile(sender, **kwargs):
	if kwargs['created']:
		user_profile = UserProfile.objects.create(user=kwargs['instance'])

post_save.connect(create_profile, sender=User)
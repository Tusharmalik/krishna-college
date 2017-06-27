from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import UserProfile
#from .models import UserProfile

class RegistrationForm(UserCreationForm):
	email = forms.EmailField(required=True)

	class Meta:
		model = User
		fields = (
				'username',
				'first_name',
				'last_name',
				'email',
				'password1',
				'password2',
			) 

	def save(self, commit=True):
		user = super(RegistrationForm, self).save(commit=False)
		user.first_name = self.cleaned_data['first_name']
		user.last_name = self.cleaned_data['last_name']
		user.email = self.cleaned_data['email']

		if commit:
			user.save()

		return user

# class EditProfileForm(UserChangeForm):

# 	class Meta:
# 		model = User
# 		#either use fields method or exclude method or both
# 		#fields method is used to include the fields and 
# 		#exclude method is used to exclude a particular fields
# 		fields = (
# 				'email',
# 				'first_name',
# 				'last_name',
# 				'password',
# 			)
# 		#exclude = ()










class ProfileForm(forms.ModelForm):
	class Meta:
		model = UserProfile
		fields = (
				'designation',
				'department',
				'masters_specialization',
				'masters_year',
				'masters_university',
				'btech_specialization',
				'btech_year',
				'btech_university',
				'teaching_experience',
				'industry_experience',
				'research_experience',
				'research_interest',
				'teaching_interest',
				'research_paper_published',
				'summary',
				'image',
			)
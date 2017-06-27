from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import RegistrationForm,ProfileForm#, EditProfileForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm, PasswordChangeForm
from django.contrib.auth import update_session_auth_hash

def signup(request):
	if request.method == 'POST':
		form = RegistrationForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('/')

	else:
		form = RegistrationForm()

		args = {'form': form}
		return render(request, "login/signup.html", args)


def view_profile(request):
	args = {'user': request.user}
	return render(request, 'login/profile.html', args)

def edit_profile(request):
	if request.method == 'POST':
		form = ProfileForm(request.POST, instance=request.user)

		if form.is_valid():
			form.save()
			return redirect('/profile')

	else:
		form = ProfileForm(instance=request.user)
		args = {'form': form}
		return render(request, 'login/edit profile.html', args)


def change_password(request):
	if request.method == 'POST':
		form = PasswordChangeForm(data=request.POST, user=request.user)

		if form.is_valid():
			form.save()
			update_session_auth_hash(request, form.user)
			return redirect('/profile')
		else:
			return redirect('/profile/password')

	else:
		form = PasswordChangeForm(user=request.user)
		args = {'form': form}
		return render(request, 'login/change_password.html', args)
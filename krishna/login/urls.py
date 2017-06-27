from django.conf.urls import url
from django.contrib.auth.views import login, logout
from . import views

app_name = 'login'
urlpatterns = [
	url(r'^login/', login, {'template_name': 'login/login.html'}, name='user_login'),
	url(r'^logout/', logout, {'template_name': 'login/logout.html'}, name='user_logout'),
	url(r'^signup/', views.signup, name='signup'),
	url(r'^profile/$', views.view_profile, name='profile'),
	url(r'^profile/edit/$', views.edit_profile, name='edit_profile'),
	url(r'^profile/password/$', views.change_password, name='change_password'),
]

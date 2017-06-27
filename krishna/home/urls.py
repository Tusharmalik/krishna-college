from django.conf.urls import url
from . import views

app_name = "home"
urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^Notice-Board/', views.notice, name='notice'),
	url(r'^Events/', views.event, name='event'),
]  

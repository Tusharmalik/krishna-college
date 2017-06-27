from django.conf.urls import url
from . import views

app_name = "about_institute"
urlpatterns = [
	url(r'^overview/', views.overview, name='overview'),
	url(r'^directors desk/', views.directors_desk, name='directors_desk'),
	url(r'^about director/$', views.director, name='director'),
	url(r'^about management/', views.about_management, name='about_management'),
	url(r'^important functionaries/', views.important_functionaries, name='important_functionaries'),
	url(r'^vision and mission/', views.vision_and_mission, name='vision_and_mission'),
	url(r'^organisation chart/', views.organisation_chart, name='organisation_chart'),
	url(r'^mandatory disclosure/', views.mandatory_disclosure, name='mandatory_disclosure'),
	url(r'^aicte approval/', views.aicte_approval, name='aicte_approval'),
]  

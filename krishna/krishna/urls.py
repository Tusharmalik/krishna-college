"""krishna URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth import views as auth_views

urlpatterns = [
    url(r'^', include('login.urls')),
    #url(r'^accounts/login/$', auth_views.login, name='login'),
    #url(r'^accounts/logout/$', auth_views.logout, name='logout'),
    url(r'^admin/', admin.site.urls),
    url(r'^',include('home.urls')),
    url(r'^about institute/',include('about_institute.urls')),
    #url(r'^admissions and registration/',include('admissions_and_registration.urls')),
    #url(r'^training and placement/',include('training_and_placement.urls')),
    #url(r'^departments/',include('departments.urls')),
    #url(r'^campus life/',include('campus_life.urls')),
    #url(r'^career/',include('career.urls')),
]

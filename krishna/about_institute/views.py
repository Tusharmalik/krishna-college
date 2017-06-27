from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from django.views import generic
from django.utils import timezone
from .models import Overview, DirectorsDesk, AboutManagement, ImportantFunctionaries, VisionAndMission, Aicte

def overview(request):
	all_overview = Overview.objects.get(pk=1)
	context = {'overview': all_overview}
	return render(request,'about_institute/overview.html',context)

def directors_desk(request):
	director = DirectorsDesk.objects.get(pk=1)
	context = {'director': director}
	return render(request,'about_institute/directors desk.html',context)

def director(request):
	return render(request,'about_institute/director.html')

def about_management(request):
	management = AboutManagement.objects.get(pk=1)
	context = {'management': management}
	return render(request,'about_institute/about management.html',context)

def important_functionaries(request):
	functionaries = ImportantFunctionaries.objects.all()
	context = {'functionaries': functionaries}
	return render(request,'about_institute/important functionaries.html',context)

def vision_and_mission(request):
	vision = VisionAndMission.objects.get(pk=1)
	context = {'vision': vision}
	return render(request,'about_institute/vision and mission.html',context)

def organisation_chart(request):
	return render(request,'about_institute/organisation chart.html')

def mandatory_disclosure(request):
	return render(request,'about_institute/mandatory disclosure.html')

def aicte_approval(request):
	aicte = Aicte.objects.all()
	context = {'aicte': aicte}
	return render(request,'about_institute/aicte.html',context)
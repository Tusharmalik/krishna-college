from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from django.views import generic
from django.utils import timezone
from .models import NoticeBoard, SlideShow, Event, Highlight

def index(request):
	latest_question_list = NoticeBoard.objects.order_by('-pub_date')[:5]
	Slide = SlideShow.objects.all()
	latest_events = Event.objects.order_by('-pub_date')[:4]
	latest_highlights = Highlight.objects.order_by('-pub_date')[:5]
	context = {'latest_question_list':latest_question_list, 'Slide':Slide, 'events': latest_events, 'highlight': latest_highlights}
	return render(request, "home/index.html", context)

def notice(request):
	all_notice = NoticeBoard.objects.all()
	context = {'all_notice':all_notice}
	return render(request, "home/AllNotice.html", context)

def event(request):
	all_event = Event.objects.all()
	context = {'all_event':all_event}
	return render(request, "home/AllEvents.html", context)
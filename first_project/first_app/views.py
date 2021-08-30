from django.shortcuts import render
from django.http import HttpResponse
from .models import Topic, WebPage, AccessRecord


# Create your views here.

def home(request):
	return render(request, 'index_page.html')


def first_app_index(request):
	return HttpResponse('<em> this is first app index page!!</em>')


def acc_records(request):
	web_pages = AccessRecord.objects.order_by('date')
	context = {
		'acc_records': web_pages
	}
	return render(request, 'first_app/acc_records.html', context)

from django.shortcuts import render
from .models import Task

from django.views import View
from django.http import JsonResponse


from django.views.generic import (
	CreateView,
	DetailView,
	ListView,
	UpdateView,
	DeleteView
)


from urlparser.helpers.WebsiteDataHelper import WebsiteDataHelper


class GetData(ListView):

	queryset = Task.objects.all() # /task/<modalname>_list.html

	print(queryset)


class ParseURLAjax(View):
    def get(self, request):
    	new_data = WebsiteDataHelper.process_url('a')
    	return JsonResponse(new_data)


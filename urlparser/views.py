from django.shortcuts import render
from .models import Task

from django.views import View
from django.http import JsonResponse


from django.views.generic import (
	ListView,
)

from urlparser.helpers.WebsiteDataHelper import WebsiteDataHelper
from django.http import HttpResponse

class GetData(ListView):

	queryset = Task.objects.values() # /task/<modalname>_list.html

	def get(self, request):
		import json
		result_list = list(self.queryset.values('title', 'description', 'siteName'))
		return HttpResponse(json.dumps(result_list), content_type="application/json")


class ParseURLAjax(View):
    def get(self, request):
    	new_data = WebsiteDataHelper.process_url('a')
    	return JsonResponse(new_data)


def urlparser(request):	
	return render(request, 'urlparser/task_page.html', {})






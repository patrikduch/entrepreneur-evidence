from django.shortcuts import render
from .models import Task

from django.views import View
from django.http import JsonResponse


from django.views.generic import (
	ListView,
)


from django.views.decorators.csrf import csrf_exempt
from urlparser.helpers.WebsiteDataHelper import WebsiteDataHelper
from django.http import HttpResponse

class GetData(ListView):

	queryset = Task.objects.values() # /task/<modalname>_list.html

	def get(self, request):
		import json
		result_list = list(self.queryset.values('title', 'description', 'siteName', 'url'))
		return HttpResponse(json.dumps(result_list), content_type="application/json")	


class ParseURLAjax(View):
	def post(self, request, *args, **kwargs):

		import json

	
		# Parse request dat
		url = request.POST['url']


		# Process website url data
		new_data = WebsiteDataHelper.process_url(url)

		if (new_data['metaTitle'] is None):
			new_data['metaTitle'] = new_data['title']



		if new_data['description'] is None:
			new_data['description'] = ''


		# Save data tu database
		Task.objects.create(description= new_data['description'], siteName=new_data['title'], title=new_data['title'], url=url);

		return JsonResponse(new_data)


def urlparser(request):	
	return render(request, 'urlparser/task_page.html', {})






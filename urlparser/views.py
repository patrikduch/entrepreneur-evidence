from django.shortcuts import render

from .models import Task


from django.views.generic import (
	CreateView,
	DetailView,
	ListView,
	UpdateView,
	DeleteView
)



# Create your views here.




class GetData(ListView):

	queryset = Task.objects.all() # /task/<modalname>_list.html

	print(queryset)






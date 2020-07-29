from django.shortcuts import render
from .models import Enterpreneur
from .forms import EnterpreneurForm, EnterpreneurRawForm



def home(request):	

	my_form = EnterpreneurRawForm()

	if (request.method == 'POST'):
		my_form = EnterpreneurRawForm(request.POST or None)

		print(my_form)

		if my_form.is_valid():
			# now that data is good
			print(my_form.cleaned_data)
		else:
			print(my_form.errors)

	
	context = {
		"form": my_form
	}

	
	return render(request, 'home.html', context)


def about(request):
	return render(request, 'about.html', {})
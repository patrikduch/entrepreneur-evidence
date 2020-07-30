from django.shortcuts import render
from .models import Enterpreneur
from .forms import EnterpreneurForm, EnterpreneurRawForm
from pages.helpers.AresFetcherHelper import AresFetcherHelper


def home(request):	

	my_form = EnterpreneurRawForm()

	if (request.method == 'POST'):
		my_form = EnterpreneurRawForm(request.POST or None)

		if my_form.is_valid():
			if AresFetcherHelper.is_ico_valid(my_form.cleaned_data["ico"]): # now that data is in proper state
				
				#Enterpreneur.objects.create(firstName='Patrik', lastName='Duch', email='duchpatrik@icloud.com', ico='09225471')
				Enterpreneur.objects.create(**my_form.cleaned_data)


				# Reset form credential after successfull submition
				my_form = EnterpreneurRawForm()


		else:
			print(my_form.errors)

	# Add form into contect
	context = {
		"form": my_form
	}

	
	return render(request, 'home.html', context)


def about(request):
	return render(request, 'about.html', {})
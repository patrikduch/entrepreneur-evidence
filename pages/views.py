from django.shortcuts import render
from .models import Enterpreneur
from .forms import EnterpreneurForm
from pages.helpers.AresFetcherHelper import AresFetcherHelper


def home(request):	

	my_form = EnterpreneurForm()

	if (request.method == 'POST'):
		my_form = EnterpreneurForm(request.POST or None)

		if my_form.is_valid():
			if AresFetcherHelper.is_ico_valid(my_form.cleaned_data["ico"]): # now that data is in proper state
				
				my_form.save()

				# Reset form credential after successfull submition
				my_form = EnterpreneurForm()
		else:
			print(my_form.errors)

	# Add form into contect
	context = {
		"form": my_form,
	}

	return render(request, 'home.html', context)


def about(request):
	return render(request, 'about.html', {})
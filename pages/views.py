from django.shortcuts import render
from .models import Enterpreneur
from .forms import EnterpreneurForm, EnterpreneurRawForm

from pages.helpers.AresFetcherHelper import AresFetcherHelper


def home(request):	

	my_form = EnterpreneurRawForm()

	if (request.method == 'POST'):
		my_form = EnterpreneurRawForm(request.POST or None)

		if my_form.is_valid():
			# now that data is good
			
			print(my_form["ico"])


			#print(my_form.cleaned_data)

			if AresFetcherHelper.is_ico_valid('09225471'):
				print("Yes")
		else:
			print(my_form.errors)

	
	context = {
		"form": my_form
	}

	
	return render(request, 'home.html', context)


def about(request):
	return render(request, 'about.html', {})
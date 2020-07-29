from django.shortcuts import render
from .models import Enterpreneur
from .forms import EnterpreneurForm


def home(request):

	if request.method == 'POST':
		form = EnterpreneurForm(request.POST or None)
		if form.is_valid():
			form.save()
		return render(request, 'home.html', {})

	else:
		all_enterpreneurs = Enterpreneur.objects.all
		return render(request, 'home.html', {"enterpreneurs": all_enterpreneurs})


def about(request):
	return render(request, 'about.html', {})
from django import forms
from .models import  Enterpreneur


class EnterpreneurForm(forms.ModelForm):

	class Meta:
		model = Enterpreneur
		fields = ['firstName', 'lastName', 'email', 'ico']



class EnterpreneurRawForm(forms.Form):

	firstName = forms.CharField(
		widget=forms.TextInput(attrs={'class': 'form-control'}),
	)
	lastName = forms.CharField(
		widget=forms.TextInput(attrs={'class': 'form-control'}),
	)
	email = forms.EmailField(
		widget=forms.EmailInput(attrs={'class': 'form-control'}),
	)
	ico = forms.CharField(
		widget=forms.TextInput(attrs={'class': 'form-control'}),
	)


	

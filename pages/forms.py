from django import forms
from .models import  Enterpreneur


class EnterpreneurForm(forms.ModelForm):

	class Meta:
		model = Enterpreneur
		fields = ['firstName', 'lastName', 'email', 'ico']



class EnterpreneurRawForm(forms.Form):

	firstName = forms.CharField(
		max_length=255,
		widget=forms.TextInput(attrs={'class': 'form-control'}),
	)
	lastName = forms.CharField(
		max_length=255,
		widget=forms.TextInput(attrs={'class': 'form-control'}),
	)
	email = forms.EmailField(
		required=False,
		max_length=255,
		widget=forms.EmailInput(attrs={'class': 'form-control'}),
	)
	ico = forms.CharField(
		label='IČO',
		max_length=8,
		widget=forms.TextInput(attrs={'class': 'form-control'}),
	)


	

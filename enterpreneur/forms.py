from django import forms
from .models import  Enterpreneur
from enterpreneur.helpers.AresFetcherHelper import AresFetcherHelper


class EnterpreneurForm(forms.ModelForm):

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


	class Meta:
		model = Enterpreneur
		fields = ['firstName', 'lastName', 'email', 'ico']


	def clean_ico(self, *args, **kwargs):

		ico = self.cleaned_data.get('ico')

		if not AresFetcherHelper.is_ico_valid(ico):
			raise forms.ValidationError('This is not a  valid ICO')

		return ico

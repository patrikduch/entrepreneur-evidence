from django import forms
from .models import  Enterpreneur


class EnterpreneurForm(forms.ModelForm):

	class Meta:
		model=Enterpreneur
		fields= ["firstName", "lastName", "email", "ico"]


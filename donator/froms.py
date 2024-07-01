from django.forms import ModelForm
from .models import Donator

class DonatorRegistationForm(ModelForm):
	class Meta:
		model = Donator
		fields= '__all__'
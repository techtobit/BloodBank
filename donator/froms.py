from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import DonatorDetails
from .constant import BLOOD_GROUP

# from django.forms import ModelForm
# from .models import Donator
# class DonatorRegistationForm(ModelForm):
# 	class Meta:
# 		model = Donator
# 		fields= '__all__'


class DonatorRegistationForm(UserCreationForm):
	blood_group=forms.ChoiceField(choices=BLOOD_GROUP)
	phone_number=forms.IntegerField()

	class Meta:
		model = User
		fields=['username','first_name', 'last_name', 'password1', 'password2', 'blood_group', 'phone_number']

	def save(self, commit = True):
		fetch_user = super(UserCreationForm, self).save(commit=False)
		if commit == True:
			fetch_user.save()
			blood_group=self.cleaned_data.get('blood_group')
			phone_number = self.cleaned_data.get('phone_number')

			DonatorDetails.objects.create(
				user=fetch_user,
				blood_group = blood_group,
				phone_number = phone_number

			)

			return fetch_user


class DonatorProfileUpdateForm(forms.ModelForm):
	# phone_number=forms.IntegerField()
	class Meta:
		model = User
		fields = ['first_name', 'last_name']

	




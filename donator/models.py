from django.db import models
from .constant import BLOOD_GROUP

class Donator(models.Model):
	full_name =models.CharField(max_length=200)
	age =models.IntegerField(blank=False)
	blood_group =models.IntegerField(choices=BLOOD_GROUP)
	# distric = 
	# state = 
	# uninion = 
	total_donated =models.IntegerField(blank=False)
	phone_number =models.IntegerField(blank=False, unique=True)
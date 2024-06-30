from django.db import models

class Donator(models.Model):
	full_name = models.CharField(max_lenght=100)
	age =  models.IntegerField(blank=False)
	# blood_group =
	# loaction = 
	# total_donated =
	# phone_number =
	# socail_media = 
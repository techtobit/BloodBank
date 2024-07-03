from django.db import models
from django.contrib.auth.models import User
from .constant import BLOOD_GROUP


class DonatorDetails(models.Model):
	user = models.OneToOneField(User, related_name='donator_account', on_delete=models.CASCADE)
	age =models.IntegerField( default=00)
	blood_group = models.CharField(max_length=15,choices=BLOOD_GROUP)
	total_donated =models.IntegerField( default=00)
	phone_number =models.IntegerField(blank=False, unique=True)


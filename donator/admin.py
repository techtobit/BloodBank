from django.contrib import admin
from .models import Donator
# Register your models here.
# admin.site.register(Donator)

@admin.register(Donator)
class DonatorAdmin(admin.ModelAdmin):
		list_display =['full_name','age','blood_group','total_donated','phone_number']

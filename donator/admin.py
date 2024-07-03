from django.contrib import admin
from .models import DonatorDetails
# Register your models here.
# admin.site.register(DonatorDetails)

@admin.register(DonatorDetails)
class DonatorAdmin(admin.ModelAdmin):
		list_display =['age','blood_group','total_donated','phone_number']

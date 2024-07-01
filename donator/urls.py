from django.contrib import admin
from django.urls import path, include
from .views import DonatorRegistationView
urlpatterns = [
		path('', DonatorRegistationView, name='singup'),
]

from django.contrib import admin
from django.urls import path, include
from .views import DonatorRegistationView, DonatorProfileUpdateView
urlpatterns = [
		path('singup/', DonatorRegistationView.as_view(), name='singup'),
		path('profile/', DonatorProfileUpdateView, name='profile'),
		# path('profile/', DonatorProfileUpdateView.as_view(), name='profile'),
]

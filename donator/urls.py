from django.contrib import admin
from django.urls import path, include
from .views import DonatorRegistationView, DonatorProfileUpdateView, DonatorLogOutView, DonatorLogInView
urlpatterns = [
		path('singup/', DonatorRegistationView.as_view(), name='singup'),
		path('logout/',  DonatorLogOutView.as_view(), name='logout'),
		path('login/',  DonatorLogInView.as_view(), name='login'),
		path('profile/', DonatorProfileUpdateView.as_view(), name='profile'),
		# path('profile/', DonatorProfileUpdateView, name='profile'),
]

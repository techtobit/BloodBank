from django.contrib import admin
from django.urls import path, include
from .views import Home
urlpatterns = [
		path('home/', Home, name='home'),
]

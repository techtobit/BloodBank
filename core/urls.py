from django.contrib import admin
from django.urls import path, include
from .views import Home
urlpatterns = [
		path("__reload__/", include("django_browser_reload.urls")),
		path('home/', Home, name='home'),
]

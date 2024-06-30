
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    # path('donator/', include('donator.urls')),
    # path('donator/', include('donator.urls')),
]

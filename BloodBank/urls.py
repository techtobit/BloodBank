
from django.contrib import admin
from django.urls import path, include
from core.views import Home

urlpatterns = [
    path('', Home, name='home'),
    path('admin/', admin.site.urls),
    path('core/', include('core.urls'))
    # path('donator/', include('donator.urls')),
    # path('donator/', include('donator.urls')),
]

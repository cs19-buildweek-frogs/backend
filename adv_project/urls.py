from django.contrib import admin
from django.urls import path, include
from django.conf.urls import include

#This is the URL Declaration. It is the url director controler. / Pablo

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
    path('api/adv/', include('adventure.urls')),
]

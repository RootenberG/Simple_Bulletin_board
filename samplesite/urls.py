"""Samplesite Routing Configuration"""
from django.contrib import admin
from django.urls import path, include
from bboard.views import index


urlpatterns = [
    path('admin/', admin.site.urls),
    path('bboard/', include('bboard.urls')),
]


from django.contrib import admin
from django.urls import path,include
from logisticsapp import views

urlpatterns = [
    path('', include('logisticsapp.urls')),
]

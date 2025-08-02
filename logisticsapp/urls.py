
from django.contrib import admin
from django.urls import path

from logisticsapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('quote/', views.Myquote, name='get-a-quote'),
    path('', views.index, name='home'),
    path('pricing/', views.pricing, name='pricing'),
    path('service/', views.service , name='service-details'),
    path('services/', views.services , name='services'),
    path('starter/', views.starter , name='starter-page'),
    path('show/', views.show , name='show'),
]

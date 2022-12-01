from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='index'),
    path('about/', views.home_about, name='about'),
    path('services/', views.home_services, name='services'),
    path('contact/', views.home_contact, name='contact'),
    path('result', views.result, name='result'),


    ]

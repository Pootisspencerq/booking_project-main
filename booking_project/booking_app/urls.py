from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('about/', views.about_view, name='about'),
    #path('booking/', views.booking_view, name='booking'),
    path('resources/', views.resources_view, name='resources'),
]

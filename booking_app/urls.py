from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from .views import register_view, login_view, logout_view

from .views import create_booking, booking_success

urlpatterns = [
    path('booking/<int:room_id>/', create_booking, name='create_booking'),
    path('booking/success/', booking_success, name='booking_success'),
    path('resources/', views.resource_list, name='resource_list'),
    path('', views.home, name='home'),
    path('rooms/<int:room_id>/', views.room_detail, name='room_detail'),
    path('rooms/create/', views.create_room, name='create_room'),
    path('', views.home, name='home'),
    path('rooms/', views.room_list, name='room_list'),  # <- додай це
    path('rooms/<int:room_id>/', views.room_detail, name='room_detail'),
    path('rooms/create/', views.create_room, name='create_room'),
    path('register/', register_view, name='register'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
] 
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
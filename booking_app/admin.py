from django.contrib import admin
from .models import Room

from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from django.contrib.admin.sites import AlreadyRegistered

CustomUser = get_user_model()


try:
    admin.site.register(CustomUser, UserAdmin)
except AlreadyRegistered:
    pass

admin.site.register(Room)
from .models import Room, Booking

admin.site.register(Booking)
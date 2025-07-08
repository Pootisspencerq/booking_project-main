from django.contrib import admin
from booking_app.models import Room, Reservation, TypeRoom

# Register your models here.
admin.site.register(Room)
admin.site.register(Reservation)
admin.site.register(TypeRoom)
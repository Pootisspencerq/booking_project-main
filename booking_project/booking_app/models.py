from django.db import models
from django.contrib.auth.models import User


class TypeRoom(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(null=True,blank=True)
    def __str__(self):
        return f"{self.title}"
    

class Room(models.Model):
    number = models.PositiveIntegerField()
    description = models.TextField(null=True,blank=True)
    place = models.PositiveIntegerField(default=1)
    price = models.PositiveIntegerField()
    image = models.ImageField(upload_to='rooms_image')
    type_room = models.ForeignKey(TypeRoom, on_delete=models.CASCADE)

    def __str__(self):
        return f"Room number: {self.number}/ price: {self.price}/ place: {self.place}"

    class Meta:
        ordering = ['price', 'number']
        verbose_name = "Room"  
        verbose_name_plural = "Rooms"


class Reservation(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    reservator = models.ForeignKey(User, on_delete=models.CASCADE)
    date_start = models.DateTimeField()
    date_end = models.DateTimeField()
    date_creation= models.DateTimeField(auto_now_add=True)
    phone = models.CharField(max_length=20)
    persons = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"data start: {self.date_start}/ data end: {self.date_end}/ data creation: {self.date_creation}"

    class Meta:
        ordering = ['date_creation','date_start','date_end']
        verbose_name = "Reservation"  
        verbose_name_plural = "Reservations"
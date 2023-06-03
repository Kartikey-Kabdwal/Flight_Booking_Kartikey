from django.db import models
from django.contrib.auth.models import User


class Flight(models.Model):
    flight_id = models.CharField(max_length=10, unique=True)
    departure_date = models.DateField()
    departure_time = models.TimeField()
    available_seats = models.PositiveIntegerField(default=60)

    def __str__(self):
        return f"Flight {self.id} - {self.departure_date} {self.departure_time}"


class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    flight = models.ForeignKey(Flight, on_delete=models.CASCADE)

    def __str__(self):
        return f"Booking {self.id} - {self.user.username} - {self.flight}"

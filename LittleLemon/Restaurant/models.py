from django.db import models
from django.core.validators import MaxValueValidator

# Create your models here.
class Booking(models.Model):
    name  = models.CharField(max_length=255)
    no_of_guests = models.SmallIntegerField(validators=[MaxValueValidator(6)])
    bookingDate = models.DateTimeField()

class Menu(models.Model):
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    inventory = models.SmallIntegerField(validators=[MaxValueValidator(6)]) 
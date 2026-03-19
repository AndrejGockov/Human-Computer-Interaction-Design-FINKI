from django.contrib.auth.models import User
from django.db import models

class Cuisine(models.Model):
    name = models.CharField(max_length=100)
    countryOfOrigin = models.CharField(max_length=100)
    description = models.TextField()
    isTrending = models.BooleanField()

class Restaurant(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    description = models.TextField()
    cuisine = models.ForeignKey(Cuisine, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images')

class Reservation(models.Model):
    STATUS = [
        ('YE', 'Confirmed'),
        ('PN', 'Pending'),
        ('NO', 'Cancelled'),
    ]

    date = models.DateTimeField()
    numGuests = models.IntegerField()
    specialRequests = models.TextField()
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    reservationHolder = models.ForeignKey(User, on_delete=models.CASCADE)
    status =  models.CharField(choices=STATUS, default='PN', max_length=2)
    price = models.IntegerField()
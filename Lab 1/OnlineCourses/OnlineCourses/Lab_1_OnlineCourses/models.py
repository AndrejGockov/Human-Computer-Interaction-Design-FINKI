from django.contrib.auth.models import User
from django.db import models

class Instructor(models.Model):
    EXPERIENCE = [
        ('B', 'Beginner'),
        ('E', 'Experienced'),
        ('P', 'Professional'),
    ]

    firstName = models.CharField(max_length=100)
    lastName = models.CharField(max_length=100)
    biography = models.TextField()
    experienceLevel = models.CharField(choices=EXPERIENCE, max_length=1, default='B')

class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    isPopular = models.BooleanField(default=False)

class Course(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    instructor = models.ForeignKey(Instructor, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    courseMaker = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images')
    price = models.IntegerField()
    availableSeats = models.IntegerField()
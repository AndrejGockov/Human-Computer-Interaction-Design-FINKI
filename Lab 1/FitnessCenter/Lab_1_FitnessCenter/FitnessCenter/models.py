from django.contrib.auth.models import User
from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    isTrending = models.BooleanField()

class Instructor(models.Model):
    EXPERIENCE = [
        ("BG", "Beginner"),
        ("CR", "Certified"),
        ("PR", "Professional"),
    ]

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    biography = models.TextField()
    experience = models.CharField(choices=EXPERIENCE, max_length=2)

class TrainingSession(models.Model):
    name = models.CharField(max_length=100)
    instructor = models.ForeignKey(Instructor, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    description = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images')
    price = models.IntegerField()
    availableSpots = models.IntegerField()
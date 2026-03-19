from django.contrib.auth.models import User
from django.db import models

# За секој автор се чува име, презиме, биографија и ниво на искуство (Почетник, Професионалец, Етаблиран автор).
class Author(models.Model):
    EXPERIENCE = [
        ("JR", "Junior"),
        ("PR", "Professional"),
        ("ET", "Established"),
    ]

    firstName = models.CharField(max_length=100)
    lastName = models.CharField(max_length=100)
    biography = models.TextField()
    experience = models.CharField(choices=EXPERIENCE, max_length=2)

# За секој жанр се чува име на жанрот (пр. Sci-Fi, Историја), опис на жанрот и информација дали е во моментов популарен (bool).
class Genre(models.Model):
    name = models.CharField(max_length=100)
    biography = models.TextField()
    isPopular = models.BooleanField(default=False)

# Креирајте Djangо апликација за менаџирање на продавница за книги.
# Секоја кинига се карактеризира со наслов, автор, кратка содржина, жанр, корисник кој ја внел книгата, слика од корицата, цена на изнајмување и број на достапни примероци.
class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
    userEntry = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.TextField()
    image = models.ImageField(upload_to='images')
    price = models.IntegerField()
    availableCopies = models.IntegerField()
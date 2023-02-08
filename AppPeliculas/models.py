from django.db import models

# Create your models here.

class Movie(models.Model):
    name = models.CharField(max_length=100)
    genre = models.CharField(max_length=50)
    year = models.PositiveSmallIntegerField()
    origin = models.CharField(max_length=50)
    duration = models.PositiveSmallIntegerField()
    director = models.CharField(max_length=100)
    cast = models.TextField()
    rating = models.FloatField()

class Actor(models.Model):
    name = models.CharField(max_length=100)
    birth_date = models.DateField()
    nationality = models.CharField(max_length=50)

class Review(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    author = models.CharField(max_length=100)
    content = models.TextField()
    rating = models.FloatField()
    pub_date = models.DateTimeField(auto_now_add=True)
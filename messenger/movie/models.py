from django.db import models
from genre.models import Genre
# Create your models here.

class Movie(models.Model):
    title = models.CharField(max_length=32)
    genres = models.ManyToManyField(Genre)
from django.db import models

# Create your models here.


class Album(models.Model):
    artist = models.CharField(max_length=500)
    album_title = models.CharField(max_length=500)
    genre = models.CharField(max_length=500)
    album_logo = models.CharField(max_length=500)  # Image url can be stored


class Songs(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    file_type = models.CharField(max_length=50)
    song_title = models.CharField(max_length=500)

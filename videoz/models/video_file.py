from django.db import models

from videoz.models.movie import Movie


class VideoFile(models.Model):
    movie = models.ForeignKey(Movie)
    name = models.CharField(max_length=255)
    path = models.CharField(max_length=255, blank=True, null=True)
    link = models.CharField(max_length=255, blank=True, null=True)
from django.db import models


class Activity(models.Model):
    title = models.CharField(max_length = 255)
    description = models.TextField()


class Entry(models.Model):
    timestamp = models.DateTimeField()

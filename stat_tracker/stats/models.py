from django.db import models

from users.models import Profile


class Activity(models.Model):
    profile = models.ForeignKey(Profile, null=True)
    title = models.CharField(max_length = 255)
    description = models.TextField()


class Entry(models.Model):
    date = models.DateField()
    count = models.IntegerField(default=0)
    activity = models.ForeignKey('Activity', null=True, related_name='stats')

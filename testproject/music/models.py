import datetime
import os

from django.db import models

# Create your models here.
from django.contrib.auth.models import Permission, User
from django.db import models

def get_file_path(instance, filename):
    """docstring"""
    image_time = datetime.datetime.now().strftime('%Y/%m/%d/%H/%M/%S')
    return os.path.join('files/' + image_time + '/', filename)

class Song(models.Model):
    name = models.CharField(max_length=100)
    duration = models.IntegerField('duration', default="00:00:00")
    created_at = models.DateTimeField(auto_now_add=True)
    media = models.FileField(blank=True, default="", upload_to=get_file_path)

    def __str__(self):
        return self.name

    class Meta:
        """Meta options for SystemParameters Model"""
        db_table = "song"


class Podcast(models.Model):
    name = models.CharField(max_length=100)
    duration = models.IntegerField('duration')
    created_at = models.DateTimeField(auto_now_add=True)
    host = models.CharField(max_length=100)
    participants = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    class Meta:
        """Meta options for SystemParameters Model"""
        db_table = "podcast"


class Audiobook(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    narrator = models.CharField(max_length=100)
    duration = models.IntegerField('duration')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    class Meta:
        """Meta options for SystemParameters Model"""
        db_table = "audiobook"

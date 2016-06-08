from __future__ import unicode_literals

from django.db import models
from django.utils import timezone

def artist_picture_path(instance, filename):
    url = "artist/" + str(instance.id) + "/" + filename
    return url

def item_picture_path(instance, filename):
    url = "items/" + str(instance.id) + "/" + filename
    return url

# Create your models here.
class artists(models.Model):
    name = models.CharField(max_length=85L, blank=True)
    artist_pic = models.ImageField(upload_to=artist_picture_path, blank=True, null=True)

    def __unicode__(self):
		if self.name:
			return self.name
		else:
			return "No name"

class items(models.Model):
    name = models.CharField(max_length=85L, blank=True)
    item_description = models.CharField(max_length=85L, blank=True)
    item_pic = models.ImageField(upload_to=item_picture_path, blank=True, null=True)
    item_price = models.IntegerField(null=True, blank=True)
    item_type = models.CharField(max_length=85L, blank=True)

    def __unicode__(self):
		if self.name:
			return self.name
		else:
			return "No name"

class Room(models.Model):
    name = models.TextField()
    label = models.SlugField(unique=True)

class Message(models.Model):
    room = models.ForeignKey(Room, related_name='messages')
    handle = models.TextField()
    message = models.TextField()
    timestamp = models.DateTimeField(default=timezone.now, db_index=True)

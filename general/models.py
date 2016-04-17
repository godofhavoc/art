from __future__ import unicode_literals

from django.db import models

def artist_picture_path(instance, filename):
    url = "artist/" + str(instance.id) + "/" + filename
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

# music/models.py
from django.db import models

class Song(models.Model):
    title = models.CharField(max_length=255)
    audio_file = models.FileField(upload_to='music/songs')

from django.db import models
from django.conf import settings
import os.path
from audiofield.fields import AudioField

# Create your models here.
class Upload(models.Model):
    audioPath = models.CharField(max_length=255)
    creatorName = models.CharField(max_length=65)
    userName = models.CharField(max_length=65)
    userPassword = models.CharField(max_length=65)
    userEmail = models.CharField(max_length=255)
    audioTitle = models.CharField(max_length=255)
    audioDescription = models.CharField(max_length=1000)
    is_favorite = models.BooleanField(default=False) #default false until user clicks on favourite

    def __str__(self):
        return self.audioPath + ' - ' + self.creatorName 

class AudioFile(models.Model):
    upload = models.ForeignKey(Upload, on_delete=models.CASCADE)
    file_type = models.CharField(max_length=10)
    
    def __str__(self):
        return self.audioTitle
        #only migrate once u change the structure of a table

#Add the audio field to your model
audio_file = AudioField(upload_to='your/upload/dir', blank=True,
                        ext_whitelist=(".mp3", ".wav", ".ogg"),
                        help_text=("Allowed type - .mp3, .wav, .ogg"))

# Add this method to your model
def audio_file_player(self):
    """audio player tag for admin"""
    if self.audio_file:
        file_url = settings.MEDIA_URL + str(self.audio_file)
        player_string = '<audio src="%s" controls>Your browser does not support the audio element.</audio>' % (file_url)
        return player_string

audio_file_player.allow_tags = True
audio_file_player.short_description = ('Audio file player')
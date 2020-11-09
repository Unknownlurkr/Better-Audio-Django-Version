from django.db import models

# Create your models here.
class Upload(models.Model):
    audioPath = models.CharField(max_length=255)
    creatorName = models.CharField(max_length=65)
    userName = models.CharField(max_length=65)
    userPassword = models.CharField(max_length=65)
    userEmail = models.CharField(max_length=255)
    audioTitle = models.CharField(max_length=255)
    audioDescription = models.CharField(max_length=1000)

    def __str__(self):
        return self.audioPath + ' - ' + self.creatorName 

class AudioFile(models.Model):
    Upload = models.ForeignKey(Upload, on_delete=models.CASCADE)
    file_type = models.CharField(max_length=10)
    
    def __str__(self):
        return self.Upload
        #only migrate once u change the structure of a table
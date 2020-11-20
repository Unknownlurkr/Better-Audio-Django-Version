from django.contrib import admin
from .models import Upload, AudioFile 

# Register your models here.
admin.site.register(Upload)
admin.site.register(AudioFile)
#now we can see the Upload db

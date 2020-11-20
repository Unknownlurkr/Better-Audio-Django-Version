#takes req and sends back an http response
#from django.http import Http404 dont need anymore with the get obj err
from django.shortcuts import render,get_object_or_404
from .models import Upload , AudioFile



#what you name here is the name of ur function
#always passing in a request index page for audio app
def index(request):
    all_audio = Upload.objects.all()
    return render(request, 'audio/index.html', {'all_audio': all_audio,})



def detail(request, audio_id):
    #in notes.txt - replacing previous try and catchstatements that is shown lines 118-121 119 
    #this line below replaces line 119 in nots.txt
    files = get_object_or_404(Upload, pk=audio_id)
    return render(request, 'audio/detail.html', {'file': files})
    #return HttpResponse("<h3>Details for Audio id: " + str(audio_id) +"</h3>")

#DISPLAY AUDIO 








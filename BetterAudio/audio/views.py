#takes req and sends back an http response
from django.http import Http404
from django.shortcuts import render
from .models import Upload



#what you name here is the name of ur function
#always passing in a request index page for audio app
def index(request):
    all_audio = Upload.objects.all()
    return render(request, 'audio/index.html', {'all_audio': all_audio,})



def detail(request, audio_id):
    try:
        file = Upload.objects.get(pk=audio_id)
    except Upload.DoesNotExist:
        raise Http404("This audio upload does not exist. Please upload your file!")
    return render(request, 'audio/detail.html', {'file': file})
    #return HttpResponse("<h3>Details for Audio id: " + str(audio_id) +"</h3>")

#DISPLAY AUDIO 








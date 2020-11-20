#create a list of urls specifcally for the audio app
from django.conf.urls import url
from . import views 
#. means same dir and look for views to import into urls

#creating rules to check what url the 
#user roles requesting
urlpatterns = [
    #url pattern: /audio/
    #how to set the audio index:
    url(r'^$', views.index, name='index'),
    #/audio/audio_id/ -. /$ ignore /
    url(r'^(?P<audio_id>[0-9]+)/$', views.detail, name='detail'),
]


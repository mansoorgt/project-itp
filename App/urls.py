from django.urls import path
from .views import *
urlpatterns = [
    path('',viewRegistraionPge,name='registration'),
    path('SpeakerForm',ReginstraionForms.speakerForm,name='speakerForm'),
    path('submitspeakerform',ReginstraionForms.submitSpeakerForm,name='submitspekerform')
    
    
]

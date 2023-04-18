from django.urls import path
from .views import *
urlpatterns = [
    path('',viewRegistraionPge,name='registration'),
    path('SpeakerForm',ReginstraionForms.speakerForm,name='speakerForm'),
    path('submitspeakerform',ReginstraionForms.submitSpeakerForm,name='submitspekerform'),
    path('InvitedDelegates',ReginstraionForms.InvitedDeligates,name='InvitedDelegates'),
     path('Applicantdelegates',ReginstraionForms.ApplicantDelegates,name='Applicantdelegates'),
    
    #email
    path('send_speaker_reg_success_mail',ReginstraionForms.send_speaker_registration_succcess_mail,name='send_speaker_reg_success_mail')
    
]

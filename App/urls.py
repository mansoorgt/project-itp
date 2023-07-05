from django.urls import path
from .views import *
urlpatterns = [
    path('',viewRegistraionPge,name='registration'),
    path('SpeakerForm',ReginstraionForms.speakerForm,name='speakerForm'),
    path('submitspeakerform',ReginstraionForms.submitSpeakerForm,name='submitspekerform'),
    path('InvitedDelegates',ReginstraionForms.InvitedDeligates,name='InvitedDelegates'),
    path('DistinguishedGuest',ReginstraionForms.Distinguished_guest,name='distinguished_guest'),
    
    path('submitInvitedform',ReginstraionForms.submitInvitedDeligateForm,name='submitInvitedform'),
     path('ApplicantDelegates',ReginstraionForms.ApplicantDelegates,name='Applicantdelegates'),
    path('submitApplicantform',ReginstraionForms.submitApplicateDelegates,name='submitApplicantform'),
    path('submitDistinguishedform',ReginstraionForms.submitDistinguished,name='submitDistinguishedform'),
    
    #email
    path('send_speaker_reg_success_mail',ReginstraionForms.send_speaker_registration_succcess_mail,name='send_speaker_reg_success_mail'),
    path('send_invited_reg_success_mail',ReginstraionForms.send_invited_registration_succcess_mail,name='send_invited_reg_success_mail'),
    path('send_applicant_reg_success_mail',ReginstraionForms.send_applicant_registration_succcess_mail,name='send_applicant_reg_success_mail'),
    path('send_destiguished_reg_success_mail',ReginstraionForms.send_Distinguished_registration_succcess_mail,name='send_destiguished_reg_success_mail'),
    path('check_valid_code',ReginstraionForms.check_urc_valid,name='check_valid_code'),
]

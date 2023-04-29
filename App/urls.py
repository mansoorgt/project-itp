from django.urls import path
from .views import *
urlpatterns = [
    path('',viewRegistraionPge,name='registration'),
    path('SpeakerForm',ReginstraionForms.speakerForm,name='speakerForm'),
    path('submitspeakerform',ReginstraionForms.submitSpeakerForm,name='submitspekerform'),
    path('InvitedDelegates',ReginstraionForms.InvitedDeligates,name='InvitedDelegates'),

    path('submitInvitedform',ReginstraionForms.submitInvitedDeligateForm,name='submitInvitedform'),
     path('Applicantdelegates',ReginstraionForms.ApplicantDelegates,name='Applicantdelegates'),
    path('submitApplicantform',ReginstraionForms.submitApplicateDelegates,name='submitApplicantform'),
    #email
    path('send_speaker_reg_success_mail',ReginstraionForms.send_speaker_registration_succcess_mail,name='send_speaker_reg_success_mail'),
    path('send_invited_reg_success_mail',ReginstraionForms.send_invited_registration_succcess_mail,name='send_invited_reg_success_mail'),
    path('send_applicant_reg_success_mail',ReginstraionForms.send_applicant_registration_succcess_mail,name='send_applicant_reg_success_mail'),
    path('check_valid_code',ReginstraionForms.check_urc_valid,name='check_valid_code'),
]

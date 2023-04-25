from django.shortcuts import render 
from django.http import HttpResponse, JsonResponse
from .models import *
from django.utils import timezone 
import json
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.core.exceptions import ValidationError
from django.core.validators import validate_email
from django.conf import settings
from django.utils.html import strip_tags
from django.core import mail
def viewRegistraionPge(request):
    return render(request,'registration.html')

class ReginstraionForms():
    
    #speaker form 
    def speakerForm(request):
        return render(request,'speaker-reg.html')
    def submitSpeakerForm(request):
        first_name=request.POST.get('first-name')
        last_name=request.POST.get('last-name')
        designation=request.POST.get('designation')
        company=request.POST.get('company')
        email=request.POST.get('email')
        mobile=request.POST.get('mobile')
        country=request.POST.get('country')
        traveling_from=request.POST.get('traveling-from')
        retun_date_time=request.POST.get('retun-date-time')
        depature_date_time=request.POST.get('depature-date-time')
       
        outline_talk=request.POST.get('outline-talk')
        passport_copy=request.FILES.get('passport-copy')
        photo_upload=request.FILES.get('photo-upload')
        ksa_visa=request.POST.get('ksa-visa')

        obj=SpeakerRegistrations.objects.create(first_name=first_name,last_name=last_name,designation=designation,company=company,
                                                email=email,mobile=mobile,country=country,traveling_from=traveling_from,retun_date_time=retun_date_time,depature_date_time=depature_date_time,ksa_visa=ksa_visa,
                                                outline_talk=outline_talk,passport_copy=passport_copy,photo_upload=photo_upload,created_at=timezone.now(),status=0,collected=0,print_status=0,approved_by=0)

        return JsonResponse({'reg_id':obj.id})
    def send_speaker_registration_succcess_mail(request):
        
        data=json.loads(request.body)
        id=data['reg_id']
        obj=SpeakerRegistrations.objects.get(id=id)
        
        try:
            validate_email(obj.email)
        except ValidationError as e:
            print("bad email, details:", e)
        else:
            
            html_contect=render_to_string("email/speaker_reg_success.html")
            email_from = settings.EMAIL_HOST_USER
            subject = 'Your registration has been submited'
            # msg= EmailMultiAlternatives(subject,'From info-events ',email_from,[obj.email])
            # msg.attach_alternative(html_contect,"text/html")
            
            mail.send_mail(subject, strip_tags(html_contect), email_from, [obj.email], html_message=html_contect,fail_silently=False)
            #msg.send()
            print('Succes mail sended')
        return JsonResponse({})
    
    #invited applicant form
    def InvitedDeligates(request):
        return render(request,'invited-delegates.html')
    
    def submitInvitedDeligateForm(request):
    
        first_name=request.POST.get('first-name')
        last_name=request.POST.get('last-name')
        designation=request.POST.get('designation')
        company=request.POST.get('company')
        email=request.POST.get('email')
        mobile=request.POST.get('mobile')
        country=request.POST.get('country')
        # traveling_from=request.POST.get('traveling-from')
        # retun_date_time=request.POST.get('retun-date-time')
        # depature_date_time=request.POST.get('depature-date-time')
       
        # outline_talk=request.POST.get('outline-talk')
        passport_copy=request.FILES.get('passport-copy')
        photo_upload=request.FILES.get('photo-upload')
        ksa_visa=request.POST.get('ksa-visa')

        obj=InvitedRegistrations.objects.create(first_name=first_name,last_name=last_name,designation=designation,company=company,
                                                 email=email,mobile=mobile,country=country,ksa_visa=ksa_visa,
                                                 passport_copy=passport_copy,photo_upload=photo_upload,created_at=timezone.now(),status=0,collected=0,print_status=0,approved_by=0)

        return JsonResponse({'reg_id':obj.id})
    
    def send_invited_registration_succcess_mail(request):
        
        data=json.loads(request.body)
        id=data['reg_id']
        obj=InvitedRegistrations.objects.get(id=id)
        
        try:
            validate_email(obj.email)
        except ValidationError as e:
            print("bad email, details:", e)
        else:
            
            html_contect=render_to_string("email/invited_reg_success.html")
            email_from = settings.EMAIL_HOST_USER
            subject = 'Your invited registration has been submited'
            # msg= EmailMultiAlternatives(subject,'From info-events ',email_from,[obj.email])
            # msg.attach_alternative(html_contect,"text/html")
            
            mail.send_mail(subject, strip_tags(html_contect), email_from, [obj.email], html_message=html_contect,fail_silently=False)
            #msg.send()
            print('Succes mail sended')
        return JsonResponse({})
    
    #aplicant form
    def ApplicantDelegates(request):
        return render(request,'applicant-delegates.html') 
    

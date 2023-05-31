from django.shortcuts import render 
from django.http import HttpResponse, JsonResponse
from .models import *
from django.utils import timezone 
import json
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.core.exceptions import ValidationError
from django.core.validators import validate_email
from project_Itp import settings
from django.utils.html import strip_tags
from django.core import mail
from Portal.models import Unique_reg_code
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
            data={"name":obj.first_name+' '+obj.last_name}
            html_contect=render_to_string("email/speaker_reg_success.html",data)
            email_from = settings.EMAIL_HOST_USER
            subject = 'Registration Status – Pending'
            # msg= EmailMultiAlternatives(subject,'From info-events ',email_from,[obj.email])
            # msg.attach_alternative(html_contect,"text/html")
            
            mail.send_mail(subject, strip_tags(html_contect), email_from, [obj.email], html_message=html_contect,fail_silently=False)
            #msg.send()
            print('Succes mail sended')
        return JsonResponse({})
    
    #invited applicant form
    def InvitedDeligates(request):
        
        m_occupations=occupations.objects.filter(status=1)
        data={'occupations':m_occupations}
        return render(request,'invited-delegates.html',data)

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
        attended_pre=request.POST.get('attend')
        passport_copy=request.FILES.get('passport-copy')
        photo_upload=request.FILES.get('photo-upload')
        ksa_visa=request.POST.get('ksa-visa')
        urc_code=request.POST.get('urc-code')
        occupation=request.POST.get('occupation')
        intrested=request.POST.get('intrested_in')
        
        if Unique_reg_code.objects.filter(code=urc_code)[0].used == 0 :
            return JsonResponse({'urc_code_exceed':True})
        
        obj=InvitedRegistrations.objects.create(first_name=first_name,last_name=last_name,designation=designation,company=company,urc_code=urc_code,
                                                 email=email,mobile=mobile,country=country,ksa_visa=ksa_visa,occupation=occupation,intrested_in=intrested,pre_attend=attended_pre,
                                                 passport_copy=passport_copy,photo_upload=photo_upload,created_at=timezone.now(),status=0,collected=0,print_status=0,approved_by=0)

        urc_used_count=Unique_reg_code.objects.filter(code=urc_code)[0].used - 1
        
        Unique_reg_code.objects.filter(code=urc_code).update(used=urc_used_count)
        
        
        return JsonResponse({'reg_id':obj.id,'urc_code_exceed':False})
    
    
    def send_invited_registration_succcess_mail(request):
        
        data=json.loads(request.body)
        id=data['reg_id']
        obj=InvitedRegistrations.objects.get(id=id)
        
        try:
            validate_email(obj.email)
        except ValidationError as e:
            print("bad email, details:", e)
        else:
            data={"name":obj.first_name+' '+obj.last_name}
            html_contect=render_to_string("email/invited_reg_success.html",data)
            email_from = settings.EMAIL_HOST_USER
            subject = 'Registration Status – Pending'
            # msg= EmailMultiAlternatives(subject,'From info-events ',email_from,[obj.email])
            # msg.attach_alternative(html_contect,"text/html")
            
            mail.send_mail(subject, strip_tags(html_contect), email_from, [obj.email], html_message=html_contect,fail_silently=False)
            #msg.send()
            print('Succes mail sended')
        return JsonResponse({})
    
    #aplicant form
    def ApplicantDelegates(request):
        m_occupations=occupations.objects.filter(status=1)
        data={'occupations':m_occupations}
        return render(request,'applicant-delegates.html',data) 
    
    def submitApplicateDelegates(request):
        first_name=request.POST.get('first-name')
        last_name=request.POST.get('last-name')
        designation=request.POST.get('designation')
        company=request.POST.get('company')
        email=request.POST.get('email')
        mobile=request.POST.get('mobile')
        country=request.POST.get('country')
        passport_copy=request.FILES.get('passport-copy')
        photo_upload=request.FILES.get('photo-upload')
        ksa_visa=request.POST.get('ksa-visa')
        attended_pre=request.POST.get('attend')
        occupation=request.POST.get('occupation')
        intrested=request.POST.get('intrested_in')
        
        
        obj=ApplicantRegistrations.objects.create(first_name=first_name,last_name=last_name,designation=designation,company=company,
                                                 email=email,mobile=mobile,country=country,ksa_visa=ksa_visa,pre_attend=attended_pre,occupation=occupation,intrested_in=intrested,
                                                 passport_copy=passport_copy,photo_upload=photo_upload,created_at=timezone.now(),status=0,collected=0,print_status=0,approved_by=0)
    
        
        return JsonResponse({'reg_id':obj.id})
    
    def send_applicant_registration_succcess_mail(request):
        print('commed')
       # data=json.loads(request.body)
        #id=data['reg_id']
        id=request.POST.get('reg_id')
        obj=ApplicantRegistrations.objects.get(id=id)
        
       
        try:
            validate_email(obj.email)
        except ValidationError as e:
            print("bad email, details:", e)
        else:
            data={"name":obj.first_name+' '+obj.last_name}
 
            html_contect=render_to_string("email/applicant_reg_success.html",data)
            email_from = settings.DEFAULT_FROM_EMAIL
            subject = 'Registration Status – Pending'

            mail.send_mail(subject, strip_tags(html_contect), from_email=email_from,recipient_list=[obj.email], html_message=html_contect,fail_silently=False)
    
           
            print('Succes mail sended')
        return JsonResponse({})
    
    def check_urc_valid(request):
        data=json.loads(request.body)
        #id=data['reg_id']
        code =data['code']
        
        valid=False
        reason=''
        if Unique_reg_code.objects.filter(code=code).exists():
            if (Unique_reg_code.objects.get(code=code).used != 0):
                   valid=True
            else:
                valid=False
                reason='This code already used or max registrations exceed'
        else:
            valid=False
            reason='This code not exists'
            
        
        
        
        return JsonResponse({'valid':valid,'reason':reason})
        

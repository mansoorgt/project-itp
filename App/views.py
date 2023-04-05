from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import *
# Create your views here.
def viewRegistraionPge(request):
    return render(request,'registration.html')

class ReginstraionForms():
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

        
        SpeakerRegistrations.objects.create(first_name=first_name,last_name=last_name,designation=designation,company=company,
                                                email=email,mobile=mobile,country=country,traveling_from=traveling_from,retun_date_time=retun_date_time,depature_date_time=depature_date_time,ksa_visa=ksa_visa,
                                                outline_talk=outline_talk,passport_copy=passport_copy,photo_upload=photo_upload)

        return JsonResponse({})
from django.http import HttpResponse, JsonResponse
from django.shortcuts import redirect, render
from .models import *
from App.models import *
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.template.loader import render_to_string
from django.db.models import Q
from django.core.mail import EmailMultiAlternatives,EmailMessage
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
import datetime
from django.core.exceptions import ValidationError
from django.core.validators import validate_email
from django.utils import timezone
from Portal.Essantials import Qrcode_generate
from django.db.models import OuterRef ,Subquery

##

from App.models import *
# Create your views here.


class registration():
    def registrion_redirect(request):
        return redirect(registration.registration_page)
    def test_email(request):
        return render(request,"email/email.html")
    def send_email(request,m_email,data):
       
        html_contect=render_to_string("email/success_email.html",data)
        email_from = settings.EMAIL_HOST_USER
        subject = 'Your Registrion has submited '
        msg= EmailMultiAlternatives(subject,'From info-events ',email_from,[m_email],cc=['contact@infoeventz.com'])
        msg.attach_alternative(html_contect,"text/html")
        msg.send()
    def registration_page(request):
        build_pass_designations=build_designation.objects.all()
        event_pass_designations=eventpass_designation.objects.all()
        vapp_pass_category=vapp_category.objects.all()
        vapp_types=vapp_vehicle_type.objects.all()
        data={'build_pass_designations':build_pass_designations,'vapp_vehicle_type':vapp_types,'event_pass_designation':event_pass_designations,'vapp_category':vapp_pass_category}
        return render(request,'register.html',data)
    #check existece 
    @csrf_exempt
    def user_check_existence(request):
        
       
        firstname=request.POST.get('firstname')
        lastname=request.POST.get('lastname')
        table=request.POST.get('table')
        
        
        if int(table) == 1 :
            if request.POST.get('event_pass') == 'False':
                event_pass=False
            else:
                event_pass=True
          
            #check existence
            if Buildpass_table.objects.filter(~Q(status=2),firstname=firstname,lastname=lastname).exists():
               
                return JsonResponse({'error':True})
                
            if Eventpass_table.objects.filter(~Q(status=2),firstname=firstname,lastname=lastname) and event_pass:
      
                return JsonResponse({'error':True})
            
        if int(table) == 2 :
            
            
            if Eventpass_table.objects.filter(~Q(status=2),firstname=firstname,lastname=lastname).exists():
   
                return JsonResponse({'error':True})
        
        if int(table) == 3 :
            
        
            if Vapp_table.objects.filter(~Q(status=2),firstname=firstname,lastname=lastname).exists():
     
                return JsonResponse({'error':True})
            
        return JsonResponse({'error':False})
    @csrf_exempt
    def build_pass_submit(request):
        firstname=request.POST.get('firstname')
        lastname=request.POST.get('lastname')
        mobile=request.POST.get('mobile')
        email=request.POST.get('email')
        desiganation=request.POST.get('desigantion')
        compoany_name=request.POST.get('comp')
        other_des=request.POST.get('other')
        
        
        if request.POST.get('event_pass') == 'False':
            event_pass=False
        else:
            event_pass=True    
        obj=Buildpass_table.objects.create(firstname=firstname,lastname=lastname,mobile=mobile,email=email,designation_id=desiganation,company_name=compoany_name,event_pass=event_pass,status=0,print_status=0,print_count=0)
        
        uid='BUP'+str(obj.id)
        obj.UID=uid
        
        if desiganation == '0':
            obj.other_designation=other_des
        obj.save()  
            
        if event_pass:
           
            file=request.FILES.get('file')
            nationality=request.POST.get('Nationality')
            id_proof_cat=request.POST.get('id_cat')
            id_proof_img=request.FILES.get('id_proof_img')
            id_proof=request.POST.get('id_proof')
            exp_date=request.POST.get('exp_date')
            file_ext=file.name.split('.')[-1]
            
            
            event_obj=Eventpass_table.objects.create(firstname=firstname,exp_date=exp_date,lastname=lastname,mobile=mobile,email=email,designation_id=desiganation,company_name=compoany_name,status=0,print_status=0,print_count=0,nationality=nationality,id_proof=id_proof,id_proof_cat=id_proof_cat,id_proof_img=id_proof_img)
            
            uid='EVP'+str(event_obj.id)
            event_obj.UID=uid
            
            file.name='EVP'+str(event_obj.id)+'.'+file_ext
            event_obj.file=file
            
            if int(id_proof_cat)==1:
                id_proof_back=request.FILES.get('id_proof_back')
                event_obj.id_proof_back_img=id_proof_back
            
           
            event_obj.save()
        #eventpass_
            
            #eventpass_image_db.objects.create(pass_id=event_obj.id,file=file)
            
        try:
            validate_email(email)
        except ValidationError as e:
            print("bad email, details:", e)
        else:
            data={'uid':obj.UID,'mobile':obj.mobile,'name':obj.firstname+' '+obj.lastname,'created_at':obj.reg_created_at,'reg':'Build Pass'}
            registration.send_email(request,email,data)

            
        return JsonResponse({})
    @csrf_exempt
    def event_pass_submit(request):
        firstname=request.POST.get('firstname')
        lastname=request.POST.get('lastname')
        mobile=request.POST.get('mobile')
        email=request.POST.get('email')
        desiganation=request.POST.get('desigantion')
        compoany_name=request.POST.get('comp')
        nationality=request.POST.get('Nationality')
        id_proof_cat=request.POST.get('id_cat')
        id_proof=request.POST.get('id_proof')
        file=request.FILES.get('file')
        id_proof_img=request.FILES.get('id_proof_img')
        exp_date=request.POST.get('exp_date')
        file_ext=file.name.split('.')[-1]
        
        # if Eventpass_table.objects.last() == None:
        #     file.name='EVP'+'0'+'.'+file_ext
        # else:
        #     file.name='EVP'+str(Eventpass_table.objects.last().id+1)+'.'+file_ext
        
        
        other_des=request.POST.get('other')
        obj=Eventpass_table.objects.create(firstname=firstname,exp_date=exp_date,lastname=lastname,mobile=mobile,email=email,designation_id=desiganation,company_name=compoany_name,status=0,print_status=0,print_count=0,nationality=nationality,id_proof=id_proof,id_proof_cat=id_proof_cat,id_proof_img=id_proof_img)
        
        uid='EVP'+str(obj.id)
        obj.UID=uid
        
        file.name='EVP'+str(obj.id)+'.'+file_ext
        obj.file=file
        
        if int(id_proof_cat)==1:
            id_proof_back=request.FILES.get('id_proof_back')
            obj.id_proof_back_img=id_proof_back
        
        obj.save()
 
        if desiganation == '0':
            obj.other_designation=other_des
        obj.save()  
        
        
        try:
            validate_email(email)
        except ValidationError as e:
            print("bad email, details:", e)
        else:
            data={'uid':obj.UID,'mobile':obj.mobile,'name':obj.firstname+' '+obj.lastname,'des':eventpass_designation.objects.get(id=desiganation).designation,'reg':'Event Pass'}
            registration.send_email(request,email,data)
    
            
        #eventpass_image_db.objects.create(pass_id=obj.id,file=file)
        
        
        return JsonResponse({})
    @csrf_exempt
    def vapp_pass_submit(request):
        firstname=request.POST.get('firstname')
        lastname=request.POST.get('lastname')
        email=request.POST.get('email')
        mobile=request.POST.get('mobile')
        vehicle_numeber=request.POST.get('number-plate')
        category_id=request.POST.get('category_id')
        compoany_name=request.POST.get('comp')
        mulkya=request.FILES.get('mulkya')
        emirates=request.FILES.get('emirate_id')
        emirates_id_back=request.FILES.get('emirates_id_back')
        type_id=request.POST.get('type')
        pass_date=request.POST.get('pass-date')
        obj=Vapp_table.objects.create(firstname=firstname,approved_date=pass_date,mulkya=mulkya,emirates_id=emirates,emirates_id_back=emirates_id_back,lastname=lastname,email=email,company_name=compoany_name,category_id=category_id,vehicle_number=vehicle_numeber,vehicle_type_id=type_id,mobile_number=mobile,status=0,print_status=0,print_count=0)
        
        uid='VAP'+str(obj.id)
        obj.UID=uid
        
        
                
        
        obj.exp_date=datetime.datetime.strptime(obj.approved_date,"%Y-%m-%d").date()+datetime.timedelta(days=7)
        obj.save()

        try:
            validate_email(email)
        except ValidationError as e:
            print("bad email, details:", e)
        else:
            data={'uid':obj.UID,'mobile':obj.mobile_number,'name':obj.firstname+' '+obj.lastname,'des':vapp_category.objects.get(id=category_id).category,'reg':'Vehicle Pass'}
            registration.send_email(request,email,data)
          
            
        return JsonResponse({})
        #obj=Buildpass_table.objects.create()
    def registration_success(request):
        return render(request,'registration_success.html')    
    
    #bulk submit
    def submit_bulk_build_pass(request):
 
        data=request.POST.getlist('data[]')
        success=False
        firstname=data[0]
        lastname=data[1]
        email=data[2]
        mobile=data[3]
        designation=data[4][0]
        comp=data[5]

        # if Buildpass_table.objects.filter(mobile=mobile).exists():
        #     success=False
        #     return JsonResponse({'success':success})
        if build_designation.objects.filter(id=designation).exists():
            obj=Buildpass_table.objects.create(firstname=firstname,lastname=lastname,mobile=mobile,email=email,designation_id=designation,company_name=comp,event_pass=0,status=0,print_status=0,print_count=0)
            uid='BUP'+str(obj.id)
            obj.UID=uid
            obj.save()
        
            success=True
        else:
            success=False
        return JsonResponse({'success':success})
    
    def submit_bulk_vapp_pass(request):
 
        data=request.POST.getlist('data[]')
        success=False
        firstname=data[0]
        lastname=data[1]
        email=data[2]
        vehical_number=data[3]
        mobile=data[4]
        comp=data[5]
        category=data[6][0]

        if Vapp_table.objects.filter(mobile_number=mobile).exists():
            success=False
            return JsonResponse({'success':success})
        
        obj=Vapp_table.objects.create(firstname=firstname,lastname=lastname,email=email,company_name=comp,category_id=category,vehicle_number=vehical_number,mobile_number=mobile,status=0,print_status=0,print_count=0)
        uid='VAP'+str(obj.id)
        obj.UID=uid
        obj.save()
        
        success=True
        return JsonResponse({'success':success})
class Login():
    def login_page(request):
        return render(request,'login.html')    
    def validitate_login(request):
        username=request.POST.get('username')
        password=request.POST.get('password')
        
        user=authenticate(username=username,password=password)
        if user is not None:
            login(request,user)
            request.session['user_role']=user_DB.objects.get(username=username).role
            request.session['user_id']=user_DB.objects.get(username=username).id

            return JsonResponse({'login':True})     
        else:
            return JsonResponse({'login':False})  
    def log_out(request):
        logout(request)
        
        return redirect(Login.login_page)
    def create_new_user_page(request):
        return render(request,'create_user.html')
    def craete_new_user(request):
        name=request.POST.get('user-name')
        email=request.POST.get('user-email')
        password=request.POST.get('user-password')
        
        
        try:
            User.objects.create_user(username=name,email=email,password=password)
            
            user_id=1
            if user_DB.objects.last():            
                user_id=user_DB.objects.last().id + 1
                            
            user_DB.objects.create(id=user_id,username=name,role=1,is_online=0)
            request.session['user_role']=1
            data={"success":True}
        except Exception as e :

            data={"success":False,'reason':str(e)}
            
        
        return JsonResponse(data)
class Dashboard():
    @login_required()
    def dashboard_page(request):
        
        speaker_count=SpeakerRegistrations.objects.filter(deleted=0).count()
        applicant_count=ApplicantRegistrations.objects.filter(deleted=0).filter(status=0).count()
        invited_count=InvitedRegistrations.objects.filter(deleted=0).filter(status=0).count()
        Distinguished_count=DistinguishedRegistrations.objects.filter(deleted=0).filter(status=0).count()
        all_count=speaker_count+applicant_count+invited_count
        accepted_count=ApplicantRegistrations.objects.filter(deleted=0,status=1).count()+InvitedRegistrations.objects.filter(deleted=0,status=1).count()
        rejected_count=ApplicantRegistrations.objects.filter(deleted=0,status=2).count()+InvitedRegistrations.objects.filter(deleted=0,status=2).count()
        
        username=request.user.username
       
        data={'username':username,'speacker_count':speaker_count,'rejected_count':rejected_count,'distinguished_count':Distinguished_count,'accepted_count':accepted_count,'all_count':all_count,'applicant_count':applicant_count,'invited_count':invited_count,'role_id':int(request.session['user_role'])}
        return render(request,'dashboard.html',data)       
class Tablepage():
    @login_required
    def table_page(request):
       
        
        #admin    
        if request.session['user_role'] == 1:
            build_table_obj=Buildpass_table.objects.all().order_by('-id')[:100]
            event_table_obj=Eventpass_table.objects.all().order_by('-id')[:100]
            vapp_table_obj=Vapp_table.objects.all().order_by('-id')[:100]

            
        
        #builpass
        build_table=[] 
        for b in build_table_obj.iterator():
            try:
                approved_by=user_DB.objects.get(id=b.approved_by).username
            except:
                approved_by='not-apporved'
                
            designation=build_designation.objects.get(id=b.designation_id).designation
            build_table.append({'name':b.firstname+' '+b.lastname,'approved_by':approved_by,'approved_by_id':b.approved_by,'firstname':b.firstname,'collected':b.collected,'lastname':b.lastname,'des_id':b.designation_id,'id':b.id,'UID':b.UID,'designation':designation,'comp':b.company_name,'exp_date':b.exp_date,'status':b.status,'print_status':b.print_status,'print_count':b.print_count,'other_des':b.other_designation,'created_at':b.reg_created_at,'remark':b.remark})
       
        #eventpass
        event_table=[]
        for e in event_table_obj.iterator():
            try:
                approved_by=user_DB.objects.get(id=e.approved_by).username
            except:
                approved_by='not-apporved'
                
            designation=eventpass_designation.objects.get(id=e.designation_id).designation
            #img=eventpass_image_db.objects.get()
            event_table.append({'name':e.firstname+' '+e.lastname,'firstname':e.firstname,'approved_by':approved_by,'approved_by_id':e.approved_by,'collected':e.collected,'lastname':e.lastname,'des_id':e.designation_id,'UID':e.UID,'id':e.id,'designation':designation,'comp':e.company_name,'exp_date':e.exp_date,'user_img':e.file,'status':e.status,'print_status':e.print_status,'print_count':e.print_count,'other_des':e.other_designation,'created_at':e.reg_created_at,'id_proof':e.id_proof,'remark':e.remark})
        #vapp_pass
        vpp_table=[]
        for v in vapp_table_obj.iterator():
            try:
                approved_by=user_DB.objects.get(id=v.approved_by).username
            except:
                approved_by='not-apporved'
                
            category=vapp_category.objects.get(id=v.category_id).category
            vpp_table.append({'name':v.firstname+' '+v.lastname,'firstname':v.firstname,'collected':v.collected,'lastname':v.lastname,'UID':v.UID,'id':v.id,'category':category,'comp':v.company_name,'exp_date':v.exp_date,'approved_date':v.approved_date,'vehicle_number':v.vehicle_number,'status':v.status,'mobile':v.mobile_number,'print_status':v.print_status,'print_count':v.print_count,'category_id':v.category_id,'created_at':v.reg_created_at,'remark':v.remark})    
        
        data={'all_tabs':True,'username':request.user.username,'build_table':build_table,'approved_by':approved_by,'approved_by_id':v.approved_by,'event_table':event_table,'vpp_table':vpp_table,'categorys':vapp_category.objects.all(),'build_pass_designations':build_designation.objects.all(),'event_pass_designations':eventpass_designation.objects.all(),'role_id':int(request.session['user_role']),'user_id':int(request.session['user_id'])}
        return render(request,'Tables.html',data) 
    @login_required
    def Speakers_reg_page(request):
   
        objs=SpeakerRegistrations.objects.filter(deleted=0).annotate(approved_by_name=Subquery(user_DB.objects.filter(id=OuterRef('approved_by')).values('username')[:1])).order_by('-id')
        data={'datas':objs,'username':request.user.username}
        return render(request,'speaker_table_main.html',data)
    
    @login_required
    def Distinguished_reg_page(request):
   
        objs=DistinguishedRegistrations.objects.filter(deleted=0).annotate(approved_by_name=Subquery(user_DB.objects.filter(id=OuterRef('approved_by')).values('username')[:1])).order_by('-id')
        data={'datas':objs,'username':request.user.username}
        return render(request,'destiguished_table_main.html',data)

    @login_required
    def invited_reg_page(request):
        filter=request.GET.get('filter')
        objs=InvitedRegistrations.objects.filter(deleted=0)
        filter_bool=False
        if filter == 'approved':
            objs=objs.filter(status=1)
            filter_bool=True
        elif filter == 'rejected':
            objs=objs.filter(status=2)
            filter_bool=True
        else:
            objs=objs.filter(status=0)
            
        datas=objs.annotate(approved_by_name=Subquery(user_DB.objects.filter(id=OuterRef('approved_by')).values('username')[:1])).order_by('-id')
        
        data={'datas':datas,'filter_bool':filter_bool,'filter_val':filter ,'page':'invited','username':request.user.username}
        return render(request,'invited_table_main.html',data)
    @login_required
    def applicant_reg_page(request):
        filter=request.GET.get('filter')
        objs=ApplicantRegistrations.objects.filter(deleted=0)
        filter_bool=False

        if filter== 'approved':
            objs=objs.filter(status=1)
            filter_bool=True
        elif filter == 'rejected':
            objs=objs.filter(status=2)
            filter_bool=True
        else:
            objs=objs.filter(status=0)
            
        datas=objs.annotate(approved_by_name=Subquery(user_DB.objects.filter(id=OuterRef('approved_by')).values('username')[:1])).order_by('-id')
        
        data={'datas':datas,'filter_bool':filter_bool,'filter_val':filter,'page':'applicant','username':request.user.username}
        return render(request,'applicant_table_main.html',data)
    
    
    def change_category_vapp(request):
        id=request.POST.get('id')
        value=request.POST.get('value')
        
        obj=Vapp_table.objects.get(id=id)
        obj.category_id=value
        obj.save()
        
        return JsonResponse({})
    #change update data
    def update_status(request):
        status=request.POST.get('status')
        table=request.POST.get('table')
        id=request.POST.get('id')
        collected=request.POST.get('collected')

       
        
        if int(table)==1:
           
            if collected != 'true':
                obj=SpeakerRegistrations.objects.get(id=id)
                obj.status=status
                if status == '1' or status == '2':
                    obj.approved_by=user_DB.objects.get(username=request.user.username).id
                obj.updated_at=timezone.now()
                obj.save()
            else:
                obj=SpeakerRegistrations.objects.get(id=id)
                obj.collected=status
                obj.updated_at=timezone.now()
                obj.save()
                
            try:
                approved_by=user_DB.objects.get(id=obj.approved_by).username
            except:
                approved_by='not-apporved'
            
            data={'sp':SpeakerRegistrations.objects.get(id=obj.id),'approved_by_name':approved_by}
            # html=render_to_string('tables/build_table.html',data) 
           
            html=render_to_string('tables/table rows/speaker_table_row.html',data)
        
        if int(table)==2:
       
            if collected != 'true':
                obj=InvitedRegistrations.objects.get(id=id)
                obj.status=status
                if status == '1' or status == '2':
                    obj.approved_by=user_DB.objects.get(username=request.user.username).id
                obj.updated_at=timezone.now()
                obj.save()
            else:
                obj=InvitedRegistrations.objects.get(id=id)
                obj.collected=status
                obj.updated_at=timezone.now()
                obj.save()
                
            try:
                approved_by=user_DB.objects.get(id=obj.approved_by).username
            except:
                approved_by='not-apporved'
            
            data={'sp':InvitedRegistrations.objects.get(id=obj.id),'approved_by_name':approved_by}
            # html=render_to_string('tables/build_table.html',data) 
           
            html=render_to_string('tables/table rows/invited_table_row.html',data)
        
        if int(table)==3:
          
            if collected != 'true':
                obj=ApplicantRegistrations.objects.get(id=id)
                obj.status=status
                
                if status == '1' or status == '2':
                    obj.approved_by=user_DB.objects.get(username=request.user.username).id
                    
                obj.updated_at=timezone.now()
                obj.save()
            else:
                obj=ApplicantRegistrations.objects.get(id=id)
                obj.collected=status
                obj.updated_at=timezone.now()
                obj.save()
                
            try:
                approved_by=user_DB.objects.get(id=obj.approved_by).username
            except:
                approved_by='not-apporved'
            
            data={'sp':ApplicantRegistrations.objects.get(id=obj.id),'approved_by_name':approved_by}
            # html=render_to_string('tables/build_table.html',data) 
           
            html=render_to_string('tables/table rows/applicant_table_row.html',data)    
        
        if int(table)==4:
           
            if collected != 'true':
                obj=DistinguishedRegistrations.objects.get(id=id)
                obj.status=status
                if status == '1' or status == '2':
                    obj.approved_by=user_DB.objects.get(username=request.user.username).id
                obj.updated_at=timezone.now()
                obj.save()
            else:
                obj=DistinguishedRegistrations.objects.get(id=id)
                obj.collected=status
                obj.updated_at=timezone.now()
                obj.save()
                
            try:
                approved_by=user_DB.objects.get(id=obj.approved_by).username
            except:
                approved_by='not-apporved'
            
            data={'sp':DistinguishedRegistrations.objects.get(id=obj.id),'approved_by_name':approved_by}
            html=render_to_string('tables/table rows/distiguished_table_row.html',data)
            
        return JsonResponse({'table_html':html})
    #update cheked box 
    def update_bulk_status(request):
        status=request.POST.get('status')
        table=request.POST.get('table')
        #id=request.POST.get('id')
        id_array=request.POST.getlist('id_array[]')
 
        #admin    
        if request.session['user_role'] == 1:
            build_table_obj=Buildpass_table.objects.all().order_by('-id')
            event_table_obj=Eventpass_table.objects.all().order_by('-id')
            vapp_table_obj=Vapp_table.objects.all().order_by('-id')
        #ifomeuser
        if request.session['user_role'] == 2:
            build_table_obj=Buildpass_table.objects.all().order_by('-id')   
            event_table_obj=Eventpass_table.objects.all().order_by('-id')  
            vapp_table_obj=Vapp_table.objects.all().order_by('-id')
            
        htmls={}
        if int(table)==1:
            
            
            for i in id_array:
             
                obj=Buildpass_table.objects.get(id=i)
                obj.status=status
                obj.updated_at=timezone.now()
                obj.save()
                
            # build_table=[]
            # for b in build_table_obj:
            #     designation=build_designation.objects.get(id=b.designation_id).designation
            #     build_table.append({'name':b.firstname+' '+b.lastname,'firstname':b.firstname,'lastname':b.lastname,'des_id':b.designation_id,'id':b.id,'UID':b.UID,'designation':designation,'comp':b.company_name,'exp_date':b.exp_date,'status':b.status,'print_status':b.print_status,'print_count':b.print_count,'other_des':b.other_designation,'created_at':b.reg_created_at,'remark':b.remark})
        
            # data={'build_table':build_table,'role_id':int(request.session['user_role']),'categorys':vapp_category.objects.all(),'user_id':int(request.session['user_id'])}
            # html=render_to_string('tables/build_table.html',data) 
            for i in id_array:
                obj=build_table_obj.get(id=i)
                designation=build_designation.objects.get(id=obj.designation_id).designation
                try:
                    approved_by=user_DB.objects.get(id=obj.approved_by).username
                except:
                    approved_by='not-apporved'
                
                data={ 'name':obj.firstname+' '+obj.lastname,'collected':obj.collected,'approved_by':approved_by,'approved_by_id':obj.approved_by,'firstname':obj.firstname,'lastname':obj.lastname,'des_id':obj.designation_id,'id':obj.id,'UID':obj.UID,'designation':designation,'comp':obj.company_name,'exp_date':obj.exp_date,'status':obj.status,'print_status':obj.print_status,'print_count':obj.print_count,'other_des':obj.other_designation,'created_at':obj.reg_created_at,'remark':obj.remark,
                'role_id':int(request.session['user_role']),'categorys':vapp_category.objects.all(),'user_id':int(request.session['user_id'])}
                html=render_to_string('tables/table rows/build_table_row.html',data)  
                htmls[i]=html
        if int(table)==2:
            
            for i in id_array:
              
                obj=Eventpass_table.objects.get(id=i)
                obj.status=status
                obj.updated_at=timezone.now()
                obj.save()
            # event_table=[]
            # for e in event_table_obj:
            #     designation=eventpass_designation.objects.get(id=e.designation_id).designation
            #     #img=eventpass_image_db.objects.get()
            #     event_table.append({'name':e.firstname+' '+e.lastname,'firstname':e.firstname,'lastname':e.lastname,'des_id':e.designation_id,'UID':e.UID,'id':e.id,'designation':designation,'comp':e.company_name,'exp_date':e.exp_date,'user_img':e.file,'status':e.status,'print_status':e.print_status,'print_count':e.print_count,'other_des':e.other_designation,'created_at':e.reg_created_at,'remark':e.remark})
        
            # data={'event_table':event_table,'role_id':int(request.session['user_role']),'user_id':int(request.session['user_id'])}
            # html=render_to_string('tables/event_table.html',data) 

            for i in id_array:
                obj=event_table_obj.get(id=i)
                designation=eventpass_designation.objects.get(id=obj.designation_id).designation
                try:
                    approved_by=user_DB.objects.get(id=obj.approved_by).username
                except:
                    approved_by='not-apporved'
                m_data={'name':obj.firstname+' '+obj.lastname,'firstname':obj.firstname,'approved_by':approved_by,'approved_by_id':obj.approved_by,'collected':obj.collected,'lastname':obj.lastname,'des_id':obj.designation_id,'UID':obj.UID,'id':obj.id,'designation':designation,'comp':obj.company_name,'exp_date':obj.exp_date,'user_img':obj.file,'status':obj.status,'print_status':obj.print_status,'print_count':obj.print_count,'other_des':obj.other_designation,'created_at':obj.reg_created_at,'remark':obj.remark,'role_id':int(request.session['user_role']),'categorys':vapp_category.objects.all(),'id_proof':obj.id_proof,'user_id':int(request.session['user_id'])}
                html=render_to_string('tables/table rows/event_table_row.html',m_data)
                htmls[i]=html
                
        if int(table)==3:
            
            for i in id_array:
              
                obj=Vapp_table.objects.get(id=i)
                obj.status=status
                obj.updated_at=timezone.now()
              
                if status == '1':
                   
                    obj.approved_date=datetime.date.today()
                    obj.exp_date=datetime.datetime.now()+datetime.timedelta(days=7)
                obj.save()
        
            # vpp_table=[]
            # for v in vapp_table_obj:
            #     category=vapp_category.objects.get(id=v.category_id).category
            #     vpp_table.append({'name':v.firstname+' '+v.lastname,'firstname':v.firstname,'lastname':v.lastname,'UID':v.UID,'id':v.id,'category':category,'comp':v.company_name,'exp_date':v.exp_date,'approved_date':v.approved_date,'vehicle_number':v.vehicle_number,'status':v.status,'mobile':v.mobile_number,'print_status':v.print_status,'print_count':v.print_count,'category_id':v.category_id,'created_at':v.reg_created_at,'remark':v.remark})
        
            # data={'vpp_table':vpp_table,'role_id':int(request.session['user_role']),'user_id':int(request.session['user_id'])}
            # html=render_to_string('tables/vapp_table.html',data)         
            for i in id_array:
                obj=vapp_table_obj.get(id=i)
                category=vapp_category.objects.get(id=obj.category_id).category
                try:
                    approved_by=user_DB.objects.get(id=obj.approved_by).username
                except:
                    approved_by='not-apporved'
                data={'name':obj.firstname+' '+obj.lastname,'firstname':obj.firstname,'approved_by':approved_by,'approved_by_id':obj.approved_by,'collected':obj.collected,'lastname':obj.lastname,'UID':obj.UID,'id':obj.id,'category':category,'comp':obj.company_name,'exp_date':obj.exp_date,'approved_date':obj.approved_date,'vehicle_number':obj.vehicle_number,'status':obj.status,'mobile':obj.mobile_number,'print_status':obj.print_status,'print_count':obj.print_count,'category_id':obj.category_id,'created_at':obj.reg_created_at,'remark':obj.remark
                    ,'categorys':vapp_category.objects.all(),'role_id':int(request.session['user_role']),'user_id':int(request.session['user_id'])
                    }
                html=render_to_string('tables/table rows/vapp_table_row.html',data)        
                htmls[i]=html

        return JsonResponse({'table_html':html,'htmls':htmls})
    
    def update_print_status(request):
        
        table=request.POST.get('table')
        id=request.POST.get('id')
        
        #admin    
        if request.session['user_role'] == 1:
            build_table_obj=Buildpass_table.objects.all().order_by('-id')
            event_table_obj=Eventpass_table.objects.all().order_by('-id')
            vapp_table_obj=Vapp_table.objects.all().order_by('-id')
        #ifomeuser
        if request.session['user_role'] == 2:
            build_table_obj=Buildpass_table.objects.all().order_by('-id')   
            event_table_obj=Eventpass_table.objects.all().order_by('-id')  
            vapp_table_obj=Vapp_table.objects.all().order_by('-id')
    
        if int(table)==1:
           
            obj=SpeakerRegistrations.objects.get(id=id)
            
            if request.POST.get('reset')=='true':
                
                if obj.print_count == 1:
                    
                    obj.print_status=0
                else:
                    
                    obj.print_count-=1    
                
            else:
                obj.print_status=1
                obj.print_count+=1
            obj.updated_at=timezone.now()
            
            obj.save()

            try:
                approved_by=user_DB.objects.get(id=obj.approved_by).username
            except:
                approved_by='not-apporved'
            data={'sp':obj,'approved_by_name':approved_by}
            html=render_to_string('tables/table rows/speaker_table_row.html',data)
           
            
       
        if int(table)==2:
            
            obj=InvitedRegistrations.objects.get(id=id)
            if request.POST.get('reset')=='true':
                if obj.print_count == 1:
                    
                    obj.print_status=0
                else:
                    
                    obj.print_count-=1
            else:
                obj.print_status=1
                obj.print_count+=1
            obj.updated_at=timezone.now()
            obj.save()
        
       
            # obj=InvitedRegistrations.objects.get(id=id)
            # designation=build_designation.objects.get(id=obj.designation_id).designation
            try:
                approved_by=user_DB.objects.get(id=obj.approved_by).username
            except:
                approved_by='not-apporved'
            data={'sp':obj,'approved_by_name':approved_by}
            html=render_to_string('tables/table rows/invited_table_row.html',data)
       
        if int(table)==3:
            
            obj=ApplicantRegistrations.objects.get(id=id)
            if request.POST.get('reset')=='true':
                if obj.print_count == 1:
                    
                    obj.print_status=0
                else:
                    
                    obj.print_count-=1
            else:
                obj.print_status=1
                obj.print_count+=1
            obj.updated_at=timezone.now()
            obj.save()
            
            
            # designation=build_designation.objects.get(id=obj.designation_id).designation
            try:
                approved_by=user_DB.objects.get(id=obj.approved_by).username
            except:
                approved_by='not-apporved'
            data={'sp':obj,'approved_by_name':approved_by}
            html=render_to_string('tables/table rows/applicant_table_row.html',data)      
        
       
        return JsonResponse({'table_html':html})
    #vapp print
    def print_vapp_vip_id(request,id):
        
        obj=Vapp_table.objects.get(id=id)
        name=obj.firstname+' '+obj.lastname
        data={'name':name,'mobile':obj.mobile_number,'comp':obj.company_name,'vehicle_num':obj.vehicle_number,'date':obj.reg_created_at,'valid_from':obj.approved_date,'exp_date':obj.exp_date}
        
        for p in vapp_category.objects.all():
            path='prints/vapp/'+p.category+'.html'
            
            if obj.category_id == p.id:
                return render(request,path,data)  
    #build print
    def print_build_id(request,id):
        
        # obj=Buildpass_table.objects.get(id=id)
        # name=obj.firstname+' '+obj.lastname
        # if obj.designation_id == 0:
        #     data={'name':name,'mobile':obj.mobile,'comp':obj.company_name,'des':obj.other_designation}
        # else:
        #     des=build_designation.objects.get(id=obj.designation_id).designation
        #     data={'name':name,'mobile':obj.mobile,'comp':obj.company_name,'des':des}
        
        
        return render(request,'prints/speaker/speaker_print.html')
    #event print
    def print_event_id(request,id):
        obj=Eventpass_table.objects.get(id=id)
        name=obj.firstname+' '+obj.lastname
        data={'name':name,'profile':obj.file.url,'UID':obj.UID,'job_title':eventpass_designation.objects.get(id=obj.designation_id).designation,'comp':obj.company_name}
        
        for p in eventpass_designation.objects.all():
            path='prints/event_pass/'+p.designation+'.html'
            
            if obj.designation_id == p.id:
                return render(request,path,data)
    #get data for bulk
    def get_data_bulk(request):
    
        id_array=request.POST.getlist('id_array[]')
        table=request.POST.get('table')
        
        updated_array=[]
        for n in id_array:
            updated_array.append(int(n))
        
        if int(table)==1:
            request.session['build_id_array']=updated_array
        if int(table)==2:
            request.session['event_id_array']=updated_array
        if int(table)==3:
            request.session['vapp_id_array']=updated_array
            
        
        return JsonResponse({})
    def print_vapp_bulk(request):
        
        deliver_print=[]
        parking=[]
        vip=[]
        accredited=[]
        valet=[]
        for p in request.session['vapp_id_array']:
            obj=Vapp_table.objects.get(id=p)
            obj.print_status=1
            obj.print_count+=1
            obj.save()
            name=obj.firstname+' '+obj.lastname
            data={'name':name,'mobile':obj.mobile_number,'comp':obj.company_name,'vehicle_num':obj.vehicle_number,'date':obj.reg_created_at,'valid_from':obj.approved_date,'exp_date':obj.exp_date}
            
            if obj.category_id==4:
                deliver_print.append(data)
            if obj.category_id == 5:
               parking.append(data)
            if obj.category_id == 1:
                vip.append(data)
            if obj.category_id== 2:
                accredited.append(data)
            if obj.category_id==3:
                valet.append(data)
                    
        data={'delivery':deliver_print,'parking':parking,'vip':vip,'accredited':accredited,'valet':valet}
        return render(request,'prints/vapp_bulk_print.html',data)
    
    def print_event_bulk(request):
        
        dic={}

        lenght=0
        for d in eventpass_designation.objects.all():
            
            m_list=[]
            des_name=d.designation
            des_name=des_name.replace(" ","")
            des_name=des_name.replace("&","")
            for p in request.session['event_id_array']:
                obj=Eventpass_table.objects.get(id=p)
                if obj.designation_id == d.id:
                    obj.print_status=1
                    obj.print_count+=1
                    obj.save()
                    name=obj.firstname+' '+obj.lastname
                    lenght+=1
                    m_list.append({'name':name,'UID':obj.UID,'comp':obj.company_name,'profile':obj.file.url})
                    dic[des_name]=m_list
    
            #data={'name':name,'mobile':obj.mobile_number,'comp':obj.company_name,'vehicle_num':obj.vehicle_number,'date':obj.reg_created_at,'valid_from':obj.approved_date,'exp_date':obj.exp_date}
             
            # if obj.category_id==4:
            #     deliver_print.append(data)
            # if obj.category_id == 5:
            #    parking.append(data)
            # if obj.category_id == 1:
            #     vip.append(data)
            
        

            
       

        data={'dic':dic}
        return render(request,'prints/event_bulk_print.html',data)

    def print_build_bulk(request):
        build_print=[]

        for p in request.session['build_id_array']:
            obj=Buildpass_table.objects.get(id=p)
            
            obj.print_status=1
            obj.print_count+=1
            obj.save()
            
            name=obj.firstname+' '+obj.lastname
            if obj.designation_id == 0:
                build_print.append({'name':name,'mobile':obj.mobile,'comp':obj.company_name,'des':obj.other_designation})
            else:
                des=build_designation.objects.get(id=obj.designation_id).designation
            
                build_print.append({'name':name,'mobile':obj.mobile,'comp':obj.company_name,'des':des})
        
        
        return render(request,'prints/build_bulk_print.html',{'build_prints':build_print})
    
    def del_registration(request):
        
        table=request.POST.get('table')
        id=request.POST.get('id')
        
    
            
        
        if int(table)==1:
           
            obj=SpeakerRegistrations.objects.get(id=id)
            
            obj.deleted=1
            obj.save()
        
            # obj=build_table_obj.get(id=id)
            # designation=build_designation.objects.get(id=obj.designation_id).designation
            # data={'name':obj.firstname+' '+obj.lastname,'firstname':obj.firstname,'lastname':obj.lastname,'des_id':obj.designation_id,'id':obj.id,'UID':obj.UID,'designation':designation,'comp':obj.company_name,'exp_date':obj.exp_date,'status':obj.status,'print_status':obj.print_status,'print_count':obj.print_count,'other_des':obj.other_designation,'created_at':obj.reg_created_at,'remark':obj.remark,
            #   'role_id':int(request.session['user_role']),'categorys':vapp_category.objects.all(),'user_id':int(request.session['user_id'])}
            # html=render_to_string('tables/table rows/build_table_row.html',data)
            
        
        if int(table)==2:
           
            obj=InvitedRegistrations.objects.get(id=id)
            
            obj.deleted=1
            obj.save()
        
            # event_table=[]
            # for e in event_table_obj:
            #     designation=eventpass_designation.objects.get(id=e.designation_id).designation
            #     #img=eventpass_image_db.objects.get()
            #     event_table.append({'name':e.firstname+' '+e.lastname,'firstname':e.firstname,'lastname':e.lastname,'des_id':e.designation_id,'UID':e.UID,'id':e.id,'designation':designation,'comp':e.company_name,'exp_date':e.exp_date,'user_img':e.file,'status':e.status,'print_status':e.print_status,'print_count':e.print_count,'other_des':e.other_designation,'created_at':e.reg_created_at,'remark':e.remark})
        
            # data={'event_table':event_table,'role_id':int(request.session['user_role']),'user_id':int(request.session['user_id'])}
            # html=render_to_string('tables/event_table.html',data) 
            # obj=event_table_obj.get(id=id)
            # designation=eventpass_designation.objects.get(id=obj.designation_id).designation
            # m_data={'name':obj.firstname+' '+obj.lastname,'firstname':obj.firstname,'lastname':obj.lastname,'des_id':obj.designation_id,'UID':obj.UID,'id':obj.id,'designation':designation,'comp':obj.company_name,'exp_date':obj.exp_date,'user_img':obj.file,'status':obj.status,'print_status':obj.print_status,'print_count':obj.print_count,'other_des':obj.other_designation,'created_at':obj.reg_created_at,'remark':obj.remark,'role_id':int(request.session['user_role']),'categorys':vapp_category.objects.all(),'user_id':int(request.session['user_id'])}
            # html=render_to_string('tables/table rows/event_table_row.html',{'data':m_data})    
        
        if int(table)==3:
           
            obj=ApplicantRegistrations.objects.get(id=id)
            
            obj.deleted=1
            obj.save()
        
        if int(table)==4:
           
            obj=DistinguishedRegistrations.objects.get(id=id)
            
            obj.deleted=1
            obj.save()

            # vpp_table=[]
            # for v in vapp_table_obj:
            #     category=vapp_category.objects.get(id=v.category_id).category
            #     vpp_table.append({'name':v.firstname+' '+v.lastname,'firstname':v.firstname,'lastname':v.lastname,'UID':v.UID,'id':v.id,'category':category,'comp':v.company_name,'exp_date':v.exp_date,'approved_date':v.approved_date,'vehicle_number':v.vehicle_number,'status':v.status,'mobile':v.mobile_number,'print_status':v.print_status,'print_count':v.print_count,'category_id':v.category_id,'created_at':v.reg_created_at,'remark':v.remark})    
        
            # data={'vpp_table':vpp_table,'role_id':int(request.session['user_role']),'user_id':int(request.session['user_id'])}
            # html=render_to_string('tables/vapp_table.html',data)
            # obj=vapp_table_obj.get(id=id)
            # category=vapp_category.objects.get(id=obj.category_id).category
            # data={'name':obj.firstname+' '+obj.lastname,'firstname':obj.firstname,'lastname':obj.lastname,'UID':obj.UID,'id':obj.id,'category':category,'comp':obj.company_name,'exp_date':obj.exp_date,'approved_date':obj.approved_date,'vehicle_number':obj.vehicle_number,'status':obj.status,'mobile':obj.mobile_number,'print_status':obj.print_status,'print_count':obj.print_count,'category_id':obj.category_id,'created_at':obj.reg_created_at,'remark':obj.remark
            #   ,'categorys':vapp_category.objects.all(),'role_id':int(request.session['user_role']),'user_id':int(request.session['user_id'])
            #   }
            # html=render_to_string('tables/table rows/vapp_table_row.html',data)
        try:
            build_last_data_id=SpeakerRegistrations.objects.last().id
        except:
            build_last_data_id=0
            
        try:
            invited_last_data_id=Eventpass_table.objects.last().id
        except:
            invited_last_data_id=0
            
        try:
            applicant_last_data_id=Vapp_table.objects.last().id
        except:
            applicant_last_data_id=0
            
        return JsonResponse({'build_last_row_data_id':build_last_data_id,'invited_last_row_data_id':invited_last_data_id,'applicant_last_row_data_id':applicant_last_data_id,})  
        
        
    #edit submit      
    def edit_submit_speaker_reg(request):
        id=request.POST.get('id')
        firstname=request.POST.get('firstname')
        lastname=request.POST.get('lastname')
        company=request.POST.get('companyname')
        designation=request.POST.get('designation')
        country=request.POST.get('country')
        travel=request.POST.get('travel')
        outline=request.POST.get('outline')
        departure_date_time=request.POST.get('departure_date_time')
        retun_date_time=request.POST.get('retun_date_time')
        profile=request.FILES.get('profile')
        passport=request.FILES.get('passport')
        
        obj=SpeakerRegistrations.objects.get(id=id)
        obj.first_name=firstname
        obj.last_name=lastname
        obj.company=company
        obj.designation=designation
        obj.country=country
        obj.traveling_from=travel
        obj.outline_talk=outline
        obj.depature_date_time=departure_date_time
        obj.retun_date_time=retun_date_time
        
        if profile != None:
            obj.photo_upload=profile
        
        if passport != None:
            obj.passport_copy=passport
            
        obj.updated_at=timezone.now()
            
        obj.save()
        
        # build_table=[]
        # for b in build_table_obj:
        #     designation=build_designation.objects.get(id=b.designation_id).designation
        #     build_table.append({'name':b.firstname+' '+b.lastname,'firstname':b.firstname,'lastname':b.lastname,'des_id':b.designation_id,'id':b.id,'UID':b.UID,'designation':designation,'comp':b.company_name,'exp_date':b.exp_date,'status':b.status,'print_status':b.print_status,'print_count':b.print_count,'other_des':b.other_designation,'created_at':b.reg_created_at,'remark':b.remark})
        
        # data={'build_table':build_table,'role_id':int(request.session['user_role']),'categorys':vapp_category.objects.all(),'user_id':int(request.session['user_id'])}
        # html=render_to_string('tables/build_table.html',data)
        obj=SpeakerRegistrations.objects.get(id=id)
        # designation=build_designation.objects.get(id=obj.designation_id).designation
        try:
            approved_by=user_DB.objects.get(id=obj.approved_by).username
        except:
            approved_by='not-apporved'
        data={'sp':obj,'approved_by_name':approved_by}
        html=render_to_string('tables/table rows/speaker_table_row.html',data)
        return JsonResponse({'table_html':html})
    
    def edit_submit_invited_reg(request):
        id=request.POST.get('id')
        firstname=request.POST.get('firstname')
        lastname=request.POST.get('lastname')
        company=request.POST.get('companyname')
        designation=request.POST.get('designation')
        country=request.POST.get('country')
        profile=request.FILES.get('profile-image')
        
        
        obj=InvitedRegistrations.objects.get(id=id)
        obj.first_name=firstname
        obj.last_name=lastname
        obj.company=company
        obj.designation=designation
        obj.country=country
        
        if profile != None:
            obj.photo_upload=profile
        
        obj.updated_at=timezone.now()
            
        obj.save()
        
            
        
        # build_table=[]
        # for b in build_table_obj:
        #     designation=build_designation.objects.get(id=b.designation_id).designation
        #     build_table.append({'name':b.firstname+' '+b.lastname,'firstname':b.firstname,'lastname':b.lastname,'des_id':b.designation_id,'id':b.id,'UID':b.UID,'designation':designation,'comp':b.company_name,'exp_date':b.exp_date,'status':b.status,'print_status':b.print_status,'print_count':b.print_count,'other_des':b.other_designation,'created_at':b.reg_created_at,'remark':b.remark})
        
        # data={'build_table':build_table,'role_id':int(request.session['user_role']),'categorys':vapp_category.objects.all(),'user_id':int(request.session['user_id'])}
        # html=render_to_string('tables/build_table.html',data)
        obj=InvitedRegistrations.objects.get(id=id)
        # designation=build_designation.objects.get(id=obj.designation_id).designation
        try:
            approved_by=user_DB.objects.get(id=obj.approved_by).username
        except:
            approved_by='not-apporved'
        data={'sp':obj,'approved_by_name':approved_by}
        html=render_to_string('tables/table rows/invited_table_row.html',data)
        return JsonResponse({'table_html':html})
    
    def edit_submit_applicant_reg(request):
        id=request.POST.get('id')
        firstname=request.POST.get('firstname')
        lastname=request.POST.get('lastname')
        company=request.POST.get('companyname')
        designation=request.POST.get('designation')
        country=request.POST.get('country')
        profile=request.FILES.get('profile-image')
        
        print(profile)
                
        obj=ApplicantRegistrations.objects.get(id=id)
        obj.first_name=firstname
        obj.last_name=lastname
        obj.company=company
        obj.designation=designation
        obj.country=country
        
        if profile != None:
            obj.photo_upload=profile
            
        obj.updated_at=timezone.now()
            
        obj.save()
        
            
        
        # build_table=[]
        # for b in build_table_obj:
        #     designation=build_designation.objects.get(id=b.designation_id).designation
        #     build_table.append({'name':b.firstname+' '+b.lastname,'firstname':b.firstname,'lastname':b.lastname,'des_id':b.designation_id,'id':b.id,'UID':b.UID,'designation':designation,'comp':b.company_name,'exp_date':b.exp_date,'status':b.status,'print_status':b.print_status,'print_count':b.print_count,'other_des':b.other_designation,'created_at':b.reg_created_at,'remark':b.remark})
        
        # data={'build_table':build_table,'role_id':int(request.session['user_role']),'categorys':vapp_category.objects.all(),'user_id':int(request.session['user_id'])}
        # html=render_to_string('tables/build_table.html',data)
        obj=ApplicantRegistrations.objects.get(id=id)
        # designation=build_designation.objects.get(id=obj.designation_id).designation
        try:
            approved_by=user_DB.objects.get(id=obj.approved_by).username
        except:
            approved_by='not-apporved'
        data={'sp':obj,'approved_by_name':approved_by}
        html=render_to_string('tables/table rows/applicant_table_row.html',data)
        return JsonResponse({'table_html':html})
    
    def edit_submit_distiguished_reg(request):
        id=request.POST.get('id')
        firstname=request.POST.get('firstname')
        lastname=request.POST.get('lastname')
        company=request.POST.get('companyname')
        designation=request.POST.get('designation')
        country=request.POST.get('country')
        travel=request.POST.get('travel')
        # outline=request.POST.get('outline')
        departure_date_time=request.POST.get('departure_date_time')
        retun_date_time=request.POST.get('retun_date_time')
        profile=request.FILES.get('profile')
        passport=request.FILES.get('passport')
        
        obj=DistinguishedRegistrations.objects.get(id=id)
        obj.first_name=firstname
        obj.last_name=lastname
        obj.company=company
        obj.designation=designation
        obj.country=country
        obj.traveling_from=travel
        # obj.outline_talk=outline
        obj.depature_date_time=departure_date_time
        obj.retun_date_time=retun_date_time
        
        if profile != None:
            obj.photo_upload=profile
        
        if passport != None:
            obj.passport_copy=passport
            
        obj.updated_at=timezone.now()
            
        obj.save()
        
        # build_table=[]
        # for b in build_table_obj:
        #     designation=build_designation.objects.get(id=b.designation_id).designation
        #     build_table.append({'name':b.firstname+' '+b.lastname,'firstname':b.firstname,'lastname':b.lastname,'des_id':b.designation_id,'id':b.id,'UID':b.UID,'designation':designation,'comp':b.company_name,'exp_date':b.exp_date,'status':b.status,'print_status':b.print_status,'print_count':b.print_count,'other_des':b.other_designation,'created_at':b.reg_created_at,'remark':b.remark})
        
        # data={'build_table':build_table,'role_id':int(request.session['user_role']),'categorys':vapp_category.objects.all(),'user_id':int(request.session['user_id'])}
        # html=render_to_string('tables/build_table.html',data)
        obj=DistinguishedRegistrations.objects.get(id=id)
        # designation=build_designation.objects.get(id=obj.designation_id).designation
        try:
            approved_by=user_DB.objects.get(id=obj.approved_by).username
        except:
            approved_by='not-apporved'
        data={'sp':obj,'approved_by_name':approved_by}
        html=render_to_string('tables/table rows/distiguished_table_row.html',data)
        return JsonResponse({'table_html':html})


    def edit_bulk(request):
        select=request.POST.get('select')
        other_des=request.POST.get('other_des')
        id_array=request.POST.getlist('id_array[]')
        comp=request.POST.get('comp')
        table=request.POST.get('table')
        
        #admin    
        if request.session['user_role'] == 1:
            build_table_obj=Buildpass_table.objects.all().order_by('-id')
            event_table_obj=Eventpass_table.objects.all().order_by('-id')
            vapp_table_obj=Vapp_table.objects.all().order_by('-id')
        #ifomeuser
        if request.session['user_role'] == 2:
            build_table_obj=Buildpass_table.objects.all().order_by('-id')   
            event_table_obj=Eventpass_table.objects.all().order_by('-id')  
            vapp_table_obj=Vapp_table.objects.all().order_by('-id')
            
        for i in id_array:
            if int(table)==1:
                obj=Buildpass_table.objects.get(id=i)
                obj.company_name=comp
                obj.updated_at=timezone.now()
                if select != '':
                    obj.designation_id=select
                    if int(select)==0:
                        obj.other_designation=other_des
                obj.save()
        
            if int(table)==2:
                obj=Eventpass_table.objects.get(id=i)
                
                obj.company_name=comp
                obj.updated_at=timezone.now()
                if select != '':
                    obj.designation_id=select
                    if int(select)==0:
                        obj.other_designation=other_des
                obj.save()
            if int(table)==3:
           
                obj=Vapp_table.objects.get(id=i)
                obj.updated_at=timezone.now()
                obj.company_name=comp
                if select !='':
                    obj.category_id=select
                    
                obj.save()
        htmls={}
        if int(table)==1:
            # build_table=[]
            # for b in build_table_obj:
            #     designation=build_designation.objects.get(id=b.designation_id).designation
            #     build_table.append({'name':b.firstname+' '+b.lastname,'firstname':b.firstname,'lastname':b.lastname,'des_id':b.designation_id,'id':b.id,'UID':b.UID,'designation':designation,'comp':b.company_name,'exp_date':b.exp_date,'status':b.status,'print_status':b.print_status,'print_count':b.print_count,'other_des':b.other_designation,'created_at':b.reg_created_at,'remark':b.remark})
        
            # data={'build_table':build_table,'role_id':int(request.session['user_role']),'categorys':vapp_category.objects.all(),'user_id':int(request.session['user_id'])}
            # html=render_to_string('tables/build_table.html',data)  
            for i in id_array:
                obj=build_table_obj.get(id=i)
                designation=build_designation.objects.get(id=obj.designation_id).designation
                try:
                    approved_by=user_DB.objects.get(id=obj.approved_by).username
                except:
                    approved_by='not-apporved'
                data={ 'name':obj.firstname+' '+obj.lastname,'firstname':obj.firstname,'approved_by':approved_by,'approved_by_id':obj.approved_by,'collected':obj.collected,'lastname':obj.lastname,'des_id':obj.designation_id,'id':obj.id,'UID':obj.UID,'designation':designation,'comp':obj.company_name,'exp_date':obj.exp_date,'status':obj.status,'print_status':obj.print_status,'print_count':obj.print_count,'other_des':obj.other_designation,'created_at':obj.reg_created_at,'remark':obj.remark,
              'role_id':int(request.session['user_role']),'categorys':vapp_category.objects.all(),'user_id':int(request.session['user_id'])}
                html=render_to_string('tables/table rows/build_table_row.html',data)  
                htmls[i]=html      
           
        if int(table)==2:
            # event_table=[]
            # for e in event_table_obj:
            #     designation=eventpass_designation.objects.get(id=e.designation_id).designation
            #     #img=eventpass_image_db.objects.get()
            #     event_table.append({'name':e.firstname+' '+e.lastname,'firstname':e.firstname,'lastname':e.lastname,'des_id':e.designation_id,'UID':e.UID,'id':e.id,'designation':designation,'comp':e.company_name,'exp_date':e.exp_date,'user_img':e.file,'status':e.status,'print_status':e.print_status,'print_count':e.print_count,'other_des':e.other_designation,'created_at':e.reg_created_at,'remark':e.remark})
        
            # data={'event_table':event_table,'role_id':int(request.session['user_role']),'user_id':int(request.session['user_id'])}
            # html=render_to_string('tables/event_table.html',data)
            for i in id_array:
                obj=event_table_obj.get(id=i)
                designation=eventpass_designation.objects.get(id=obj.designation_id).designation
                try:
                    approved_by=user_DB.objects.get(id=obj.approved_by).username
                except:
                    approved_by='not-apporved'
                data={'name':obj.firstname+' '+obj.lastname,'firstname':obj.firstname,'approved_by':approved_by,'approved_by_id':obj.approved_by,'collected':obj.collected,'lastname':obj.lastname,'des_id':obj.designation_id,'UID':obj.UID,'id':obj.id,'designation':designation,'comp':obj.company_name,'exp_date':obj.exp_date,'user_img':obj.file,'status':obj.status,'print_status':obj.print_status,'print_count':obj.print_count,'other_des':obj.other_designation,'created_at':obj.reg_created_at,'remark':obj.remark,'role_id':int(request.session['user_role']),'categorys':vapp_category.objects.all(),'id_proof':obj.id_proof,'user_id':int(request.session['user_id'])}
                html=render_to_string('tables/table rows/event_table_row.html',data)
                htmls[i]=html
        if int(table)==3:
            # vpp_table=[]
            # for v in vapp_table_obj:
            #     category=vapp_category.objects.get(id=v.category_id).category
            #     vpp_table.append({'name':v.firstname+' '+v.lastname,'firstname':v.firstname,'lastname':v.lastname,'UID':v.UID,'id':v.id,'category':category,'comp':v.company_name,'exp_date':v.exp_date,'approved_date':v.approved_date,'vehicle_number':v.vehicle_number,'status':v.status,'mobile':v.mobile_number,'print_status':v.print_status,'print_count':v.print_count,'category_id':v.category_id,'created_at':v.reg_created_at,'remark':v.remark})    
        
            # data={'categorys':vapp_category.objects.all(),'vpp_table':vpp_table,'role_id':int(request.session['user_role']),'user_id':int(request.session['user_id'])}
            # html=render_to_string('tables/vapp_table.html',data)
            for i in id_array:
                obj=vapp_table_obj.get(id=i)
                category=vapp_category.objects.get(id=obj.category_id).category
                try:
                    approved_by=user_DB.objects.get(id=obj.approved_by).username
                except:
                    approved_by='not-apporved'
                    
                data={'name':obj.firstname+' '+obj.lastname,'firstname':obj.firstname,'approved_by':approved_by,'approved_by_id':obj.approved_by,'collected':obj.collected,'lastname':obj.lastname,'UID':obj.UID,'id':obj.id,'category':category,'comp':obj.company_name,'exp_date':obj.exp_date,'approved_date':obj.approved_date,'vehicle_number':obj.vehicle_number,'status':obj.status,'mobile':obj.mobile_number,'print_status':obj.print_status,'print_count':obj.print_count,'category_id':obj.category_id,'created_at':obj.reg_created_at,'remark':obj.remark
                    ,'categorys':vapp_category.objects.all(),'role_id':int(request.session['user_role']),'user_id':int(request.session['user_id'])
                    }
                html=render_to_string('tables/table rows/vapp_table_row.html',data)        
                htmls[i]=html
        return JsonResponse({'table_html':html,'htmls':htmls})
    
    def edit_bulk_event(request):
        select=request.POST.get('select')
        other_des=request.POST.get('other_des')
        id_array=request.POST.getlist('id_array[]')
        
        for i in id_array:
           
            obj=Eventpass_table.objects.get(id=i)
            obj.designation_id=select
            if int(select)==0:
                obj.other_designation=other_des

                
            obj.save()    

        if request.session['user_role'] == 1:
            event_table_obj=Eventpass_table.objects.all().order_by('-id')
            
        #ifomeuser
        if request.session['user_role'] == 2:
            event_table_obj=Eventpass_table.objects.all().order_by('-id')   
            
           
        event_table=[]
        for e in event_table_obj:
            designation=eventpass_designation.objects.get(id=e.designation_id).designation
            try:
                approved_by=user_DB.objects.get(id=e.approved_by).username
            except:
                approved_by='not-apporved'
                #img=eventpass_image_db.objects.get()
            event_table.append({'name':e.firstname+' '+e.lastname,'firstname':e.firstname,'approved_by':approved_by,'approved_by_id':e.approved_by,'lastname':e.lastname,'des_id':e.designation_id,'UID':e.UID,'id':e.id,'designation':designation,'comp':e.company_name,'exp_date':e.exp_date,'user_img':e.file,'status':e.status,'print_status':e.print_status,'print_count':e.print_count,'other_des':e.other_designation,'created_at':e.reg_created_at,'id_proof':e.id_proof,'remark':e.remark})
        
        data={'event_table':event_table,'role_id':int(request.session['user_role']),'categorys':vapp_category.objects.all(),'user_id':int(request.session['user_id'])}
        html=render_to_string('tables/event_table.html',data)
        
        
        
        return JsonResponse({'table_html':html})
    
    def edit_submit_event_pass(request):
        id=request.POST.get('id')
        firstname=request.POST.get('firstname')
        lastname=request.POST.get('lastname')
        comp=request.POST.get('comp')
        des_id=request.POST.get('des_id')
        id_proof=request.POST.get('id_proof')
        exp_date=request.POST.get('exp_date')
        exp_date=datetime.datetime.strptime(exp_date,"%d-%m-%Y").date()
        profile_img=request.FILES.get('profile_img')
        front_id_img=request.FILES.get('front_id')
        back_id_img=request.FILES.get('back_id')
        
        
        obj=Eventpass_table.objects.get(id=id)
        obj.firstname=firstname
        obj.lastname=lastname
        obj.company_name=comp
        obj.id_proof=id_proof
        obj.designation_id=des_id
        obj.updated_at=timezone.now()
        if exp_date != '': 
            obj.exp_date=exp_date
        
        # if obj.exp_date != exp_date:
        #     m_exp_date=datetime.datetime.strptime(exp_date, "%Y-%m-%d").date()
        #     obj.exp_date=m_exp_date+datetime.timedelta(days=1)
        
        if des_id == '0':
            other_des=request.POST.get('other_des')
            obj.other_designation=other_des
        if profile_img !=None:
            file_ext=profile_img.name.split('.')[-1]
            profile_img.name='EVP'+str(obj.id)+'.'+file_ext
            obj.file=profile_img
        
        if front_id_img !=None:
            obj.id_proof_img=front_id_img
            
        if back_id_img !=None:
            obj.id_proof_back_img=back_id_img
            
        obj.save()
        
        if request.session['user_role'] == 1:
            event_table_obj=Eventpass_table.objects.all().order_by('-id')
            
        #ifomeuser
        if request.session['user_role'] == 2:
            event_table_obj=Eventpass_table.objects.all().order_by('-id')   
            
           
        # event_table=[]
        # for e in event_table_obj:
        #     designation=eventpass_designation.objects.get(id=e.designation_id).designation
        #         #img=eventpass_image_db.objects.get()
        #     event_table.append({'name':e.firstname+' '+e.lastname,'firstname':e.firstname,'lastname':e.lastname,'des_id':e.designation_id,'UID':e.UID,'id':e.id,'designation':designation,'comp':e.company_name,'exp_date':e.exp_date,'user_img':e.file,'status':e.status,'print_status':e.print_status,'print_count':e.print_count,'other_des':e.other_designation,'created_at':e.reg_created_at,'remark':e.remark})
        
        
        obj=event_table_obj.get(id=id)
        designation=eventpass_designation.objects.get(id=obj.designation_id).designation
        try:
            approved_by=user_DB.objects.get(id=obj.approved_by).username
        except:
            approved_by='not-apporved'
        m_data={'name':obj.firstname+' '+obj.lastname,'firstname':obj.firstname,'approved_by':approved_by,'approved_by_id':obj.approved_by,'collected':obj.collected,'lastname':obj.lastname,'des_id':obj.designation_id,'UID':obj.UID,'id':obj.id,'designation':designation,'comp':obj.company_name,'exp_date':obj.exp_date,'user_img':obj.file,'status':obj.status,'print_status':obj.print_status,'print_count':obj.print_count,'other_des':obj.other_designation,'created_at':obj.reg_created_at,'remark':obj.remark,'role_id':int(request.session['user_role']),'categorys':vapp_category.objects.all(),'id_proof':obj.id_proof,'user_id':int(request.session['user_id'])}
        html=render_to_string('tables/table rows/event_table_row.html',m_data)
        
        
        # data={'event_table':event_table,'role_id':int(request.session['user_role']),'categorys':vapp_category.objects.all(),'user_id':int(request.session['user_id'])}
        # html=render_to_string('tables/event_table.html',data)
        
        
        
        return JsonResponse({'table_html':html})
    
    def edit_submit_vapp_pass(request):
        id=request.POST.get('id')
        firstname=request.POST.get('firstname')
        lastname=request.POST.get('lastname')
        vehicle_number=request.POST.get('vehicle_number')
        comp=request.POST.get('comp')
        mobile=request.POST.get('mobile')
        cat_id=request.POST.get('cat_id')
        valid_date=request.POST.get('valid_date')
        valid_from=request.POST.get('valid_from')
        fron_id=request.FILES.get('front_id')
        back_id=request.FILES.get('back_id')
        mulkya=request.FILES.get('mulkya')
        
        obj=Vapp_table.objects.get(id=id)
        obj.firstname=firstname
        obj.lastname=lastname
        obj.company_name=comp
        obj.vehicle_number=vehicle_number
        obj.mobile_number=mobile
        obj.category_id=cat_id
        obj.updated_at=timezone.now()
        if valid_date!='':
           
            obj.exp_date=valid_date
        if valid_from!='':
            obj.approved_date=valid_from
        
        if fron_id != None:
            obj.emirates_id=fron_id
        if back_id !=None:
            obj.emirates_id_back=back_id
        if mulkya != None:
            obj.mulkya=mulkya
            
        obj.save()
        
        if request.session['user_role'] == 1:
            vapp_table_obj=Vapp_table.objects.all().order_by('-id')
            
        #ifomeuser
        if request.session['user_role'] == 2:
            vapp_table_obj=Vapp_table.objects.all().order_by('-id')   
            
           
        # vpp_table=[]
        # for v in vapp_table_obj:
        #     category=vapp_category.objects.get(id=v.category_id).category
        #     vpp_table.append({'name':v.firstname+' '+v.lastname,'firstname':v.firstname,'lastname':v.lastname,'UID':v.UID,'id':v.id,'category':category,'comp':v.company_name,'exp_date':v.exp_date,'approved_date':v.approved_date,'vehicle_number':v.vehicle_number,'status':v.status,'mobile':v.mobile_number,'print_status':v.print_status,'print_count':v.print_count,'category_id':v.category_id,'created_at':v.reg_created_at,'remark':v.remark})
        
        # data={'categorys':vapp_category.objects.all(),'vpp_table':vpp_table,'role_id':int(request.session['user_role']),'user_id':int(request.session['user_id'])}
        # html=render_to_string('tables/vapp_table.html',data)
        obj=vapp_table_obj.get(id=id)
        category=vapp_category.objects.get(id=obj.category_id).category
        try:
            approved_by=user_DB.objects.get(id=obj.approved_by).username
        except:
            approved_by='not-apporved'
                    
        data={'name':obj.firstname+' '+obj.lastname,'firstname':obj.firstname,'approved_by':approved_by,'approved_by_id':obj.approved_by,'collected':obj.collected,'lastname':obj.lastname,'UID':obj.UID,'id':obj.id,'category':category,'comp':obj.company_name,'exp_date':obj.exp_date,'approved_date':obj.approved_date,'vehicle_number':obj.vehicle_number,'status':obj.status,'mobile':obj.mobile_number,'print_status':obj.print_status,'print_count':obj.print_count,'category_id':obj.category_id,'created_at':obj.reg_created_at,'remark':obj.remark
              ,'categorys':vapp_category.objects.all(),'role_id':int(request.session['user_role']),'user_id':int(request.session['user_id'])
              }
        html=render_to_string('tables/table rows/vapp_table_row.html',data)
        
        return JsonResponse({'table_html':html})
    def get_profile_details(request):
        
        id=request.POST.get('id')
        table=request.POST.get('table')
     
      
        if int(table)==1:
            obj=SpeakerRegistrations.objects.get(id=id)
            data={'id':obj.id,'uid':obj.id,'name':obj.first_name+' '+obj.last_name,'firstname':obj.first_name,'lastname':obj.last_name,'mobile':obj.mobile,'email':obj.email,'created_at':obj.created_at.date(),'comp':obj.company,'des':obj.designation,'status':obj.status,'profile_image':obj.photo_upload.url,'passport':obj.passport_copy.url,'travel':obj.traveling_from,'outline':obj.outline_talk,'depature_time':obj.depature_date_time.strftime("%d-%m-%y %I:%M %p"),'return_time':obj.retun_date_time.strftime("%d-%m-%y %I:%M %p"),'depature_time_iso':obj.depature_date_time,'return_time_iso':obj.retun_date_time,'country':obj.country,'ksa_visa':obj.ksa_visa,'remark':obj.remark,'photo_upload':str(obj.photo_upload),'passport_str':str(obj.passport_copy),'salutation':obj.salutation,'desiganation':obj.designation}
        
        if int(table)==2:
            obj=InvitedRegistrations.objects.get(id=id)
            data={'id':obj.id,'uid':obj.id,'name':obj.first_name+' '+obj.last_name,'firstname':obj.first_name,'lastname':obj.last_name,'mobile':obj.mobile,'email':obj.email,'created_at':obj.created_at.date(),'comp':obj.company,'des':obj.designation,'status':obj.status,'profile_image':obj.photo_upload.url,'country':obj.country,'ksa_visa':obj.ksa_visa,'intrested':obj.intrested_in,'remark':obj.remark,'photo_upload':str(obj.photo_upload),'passport_id':obj.passport_id,'salutation':obj.salutation,'desiganation':obj.designation}
        
        if int(table)==3:
            obj=ApplicantRegistrations.objects.get(id=id)
           # salutation=occupations.objects.get(id=obj.occupation).occupation_name
            data={'id':obj.id,'uid':obj.id,'name':obj.first_name+' '+obj.last_name,'firstname':obj.first_name,'lastname':obj.last_name,'mobile':obj.mobile,'email':obj.email,'created_at':obj.created_at.date(),'comp':obj.company,'des':obj.designation,'status':obj.status,'profile_image':obj.photo_upload.url,'country':obj.country,'ksa_visa':obj.ksa_visa,'pre_attand':obj.pre_attend,'remark':obj.remark,'photo_upload':str(obj.photo_upload),'passport_id':obj.passport_id,'salutation':obj.salutation,'desiganation':obj.designation}
        
        if int(table)==4:
            obj=DistinguishedRegistrations.objects.get(id=id)
            data={'id':obj.id,'uid':obj.id,'name':obj.first_name+' '+obj.last_name,'firstname':obj.first_name,'lastname':obj.last_name,'mobile':obj.mobile,'email':obj.email,'created_at':obj.created_at.date(),'comp':obj.company,'des':obj.designation,'status':obj.status,'profile_image':obj.photo_upload.url,'passport':obj.passport_copy.url,'travel':obj.traveling_from,'depature_time':obj.depature_date_time.strftime("%d-%m-%y %I:%M %p"),'return_time':obj.retun_date_time.strftime("%d-%m-%y %I:%M %p"),'depature_time_iso':obj.depature_date_time,'return_time_iso':obj.retun_date_time,'country':obj.country,'ksa_visa':obj.ksa_visa,'remark':obj.remark,'photo_upload':str(obj.photo_upload),'passport_str':str(obj.passport_copy),'salutation':obj.salutation,'desiganation':obj.designation}
        
     
        return JsonResponse(data)

    def get_img_urls(request):
        array=request.GET.getlist('uid_array[]')
        
        urls=[]
        for i in array:
    
            
            urls.append(Eventpass_table.objects.get(UID=i).file.url)
    
        return JsonResponse({'urls':urls})
    def change_remark(request):
        
        id=request.POST.get('id')
        Table=request.POST.get('table')
        value=request.POST.get('value')
        
        if int(Table)==1:
       
            obj=SpeakerRegistrations.objects.get(id=id)
            obj.remark=value
            obj.save()
        
        if int(Table)==2:
     
            obj=InvitedRegistrations.objects.get(id=id)
            obj.remark=value
            obj.save()
        
        if int(Table)==3:
          
            obj=ApplicantRegistrations.objects.get(id=id)
            obj.remark=value
            obj.save() 
        if int(Table)==4:
          
            obj=DistinguishedRegistrations.objects.get(id=id)
            obj.remark=value
            obj.save()   
            
        return JsonResponse({}) 
    #email send
        # rejection mail send
    def send_reason_mail(request):
        reason=request.POST.get('reason')
        table=request.POST.get('table')
        id_array=request.POST.getlist('id_array[]')
        rejected_by_photo=request.POST.get('photo_rejection')    
        
            
        for i in id_array:
            if int(table)==1:
                obj=SpeakerRegistrations.objects.get(id=i)
                obj.remark=reason
                obj.save()
                data={'uid':'SPK-'+str(obj.id),'mobile':obj.mobile,'name':obj.first_name+' '+obj.last_name,'created_at':obj.created_at,'reg':'Speaker','reason':reason}
            if int(table)==2:
                obj=InvitedRegistrations.objects.get(id=i)
                obj.remark=reason
                obj.save()
                data={'uid':'INV-'+str(obj.id),'mobile':obj.mobile,'name':obj.first_name+' '+obj.last_name,'created_at':obj.created_at,'reg':'invited','reason':reason}
            if int(table)==3:
                obj=ApplicantRegistrations.objects.get(id=i)
                obj.remark=reason
                obj.save()
                data={'uid':'APL-'+str(obj.id),'mobile':obj.mobile,'name':obj.first_name+' '+obj.last_name,'created_at':obj.created_at,'reg':'Applicant','reason':reason}   
            if int(table)==4:
                obj=DistinguishedRegistrations.objects.get(id=i)
                obj.remark=reason
                obj.save()
                data={'uid':'DIG-'+str(obj.id),'mobile':obj.mobile,'name':obj.first_name+' '+obj.last_name,'created_at':obj.created_at,'reg':'Distinguished','reason':reason}
            try:
                validate_email(obj.email)
            except ValidationError as e:
                print("bad email, details:", e)
            else:
                
                if rejected_by_photo == 'true':
                    html_contect=render_to_string("email/email_reject_by_photo.html",data)
                else:
                    html_contect=render_to_string("email/email_reject.html",data)
                    
                email_from = settings.EMAIL_HOST_USER
                subject = 'Registration Status – Update'
                #msg=EmailMessage(subject=subject,from_email=email_from,to=[obj.email],body='TESTXXX')
                msg= EmailMultiAlternatives(subject,'From info-events ',email_from,[obj.email])
                msg.attach_alternative(html_contect,"text/html")
                msg.send()
               
                
        # if int(table)==1:
        #     data=Tablepage.update_front_page(request,1)
        # if int(table)==2:
        #     data=Tablepage.update_front_page(request,2)
        # if int(table)==3:
        #     data=Tablepage.update_front_page(request,3)
    
        
        return JsonResponse({})
        
        #approved mail send
    def send_approved_mail(request):
        
        table=request.POST.get('table')
        id_array=request.POST.getlist('id_array[]')
        
        
            
        for i in id_array:
            if int(table)==1:
                obj=SpeakerRegistrations.objects.get(id=i)
                qr_url=Qrcode_generate(filename='SPK-'+str(obj.id),data={'name':obj.first_name+' '+obj.last_name,'designation':obj.designation,'country':obj.country,'email':obj.email}).url
                data={'uid':'SPK-'+str(obj.id),'qr_url':qr_url,'mobile':obj.mobile,'name':obj.first_name+' '+obj.last_name,'created_at':obj.created_at,'reg':'Speaker'}
            if int(table)==2:
                obj=InvitedRegistrations.objects.get(id=i)
                qr_url=Qrcode_generate(filename='INV-'+str(obj.id),data=obj.id).url
          
                data={'uid':'INV-'+str(obj.id),'qr_url':qr_url,'mobile':obj.mobile,'name':obj.first_name+' '+obj.last_name,'created_at':obj.created_at,'reg':'Speaker'}
            if int(table)==3:
                obj=ApplicantRegistrations.objects.get(id=i)
                qr_url=Qrcode_generate(filename='APL-'+str(obj.id),data=obj.id).url
                data={'uid':'APL-'+str(obj.id),'qr_url':qr_url,'mobile':obj.mobile,'name':obj.first_name+' '+obj.last_name,'created_at':obj.created_at,'reg':'Speaker'}   
            if int(table)==4:
                obj=DistinguishedRegistrations.objects.get(id=i)
                qr_url=Qrcode_generate(filename='DIG-'+str(obj.id),data={'name':obj.first_name+' '+obj.last_name,'designation':obj.designation,'country':obj.country,'email':obj.email}).url
                data={'uid':'DIG-'+str(obj.id),'qr_url':qr_url,'mobile':obj.mobile,'name':obj.first_name+' '+obj.last_name,'created_at':obj.created_at,'reg':'Distinguished'}
                
            try:
                validate_email(obj.email)
            except ValidationError as e:
                print("bad email, details:", e)
            else:
                
                html_contect=render_to_string("email/email_approved.html",data)
                email_from = settings.EMAIL_HOST_USER
                subject = 'Registration Status - Confirmed'
                #msg=EmailMessage(subject=subject,from_email=email_from,to=[obj.email],body='TESTXXX')
                
                msg= EmailMultiAlternatives(subject,'From info-events ',email_from,[obj.email],)
                msg.attach_alternative(html_contect,"text/html")
                msg.send()
              
            
        return JsonResponse({'data':'data'})
    def send_undo_mail(request):
        
        id=request.GET.get('id')
        table=request.GET.get('table')
        
        if int(table)==1:
            obj=SpeakerRegistrations.objects.get(id=id)
        if int(table)==2:
            obj=InvitedRegistrations.objects.get(id=id)
        if int(table)==3:
            obj=ApplicantRegistrations.objects.get(id=id)
            
            
            
        try:
            validate_email(obj.email)
        except ValidationError as e:
            print("bad email, details:", e)
        else:
            
            html_contect=render_to_string("email/test_mail.html",{'content':'Undo mail'})
            email_from = settings.EMAIL_HOST_USER
            subject = 'Application status Has been Undo'
            #msg=EmailMessage(subject=subject,from_email=email_from,to=[obj.email],body='TESTXXX')
            
            msg= EmailMultiAlternatives(subject,'From info-events ',email_from,[obj.email],)
            msg.attach_alternative(html_contect,"text/html")
            msg.send()
          
            
        return JsonResponse({})
    def update_front_page(request,table):
        # #admin    
        # if request.session['user_role'] == 1:
        #     build_table_obj=Buildpass_table.objects.all().order_by('-id')
        #     event_table_obj=Eventpass_table.objects.all().order_by('-id')
        #     vapp_table_obj=Vapp_table.objects.all().order_by('-id')
        # #ifomeuser
        # if request.session['user_role'] == 2:
        #     build_table_obj=Buildpass_table.objects.all().order_by('-id')   
        #     event_table_obj=Eventpass_table.objects.all().order_by('-id')  
        #     vapp_table_obj=Vapp_table.objects.all().order_by('-id')
            
        
        if int(table)==1:
            
            objs=SpeakerRegistrations.objects.filter(deleted=0).annotate(approved_by_name=Subquery(user_DB.objects.filter(id=OuterRef('approved_by')).values('username')[:1])).order_by('-id')
            data={'datas':objs,'username':request.user.username}
        
            html=render_to_string('tables/speaker_table.html',data) 
        
        if int(table)==2:
            
            event_table=[]
            for e in event_table_obj:
                designation=eventpass_designation.objects.get(id=e.designation_id).designation
                try:
                    approved_by=user_DB.objects.get(id=e.approved_by).username
                except:
                    approved_by='not-apporved'
                    
                #img=eventpass_image_db.objects.get()
                event_table.append({'name':e.firstname+' '+e.lastname,'firstname':e.firstname,'approved_by':approved_by,'approved_by_id':e.approved_by,'lastname':e.lastname,'des_id':e.designation_id,'UID':e.UID,'id':e.id,'designation':designation,'comp':e.company_name,'exp_date':e.exp_date,'user_img':e.file,'status':e.status,'print_status':e.print_status,'print_count':e.print_count,'other_des':e.other_designation,'created_at':e.reg_created_at,'id_proof':e.id_proof,'remark':e.remark})
        
            data={'event_table':event_table,'role_id':int(request.session['user_role']),'user_id':int(request.session['user_id'])}
            html=render_to_string('tables/event_table.html',data)     
        
        if int(table)==3:
            
            vpp_table=[]
            for v in vapp_table_obj:
                category=vapp_category.objects.get(id=v.category_id).category
                try:
                    approved_by=user_DB.objects.get(id=v.approved_by).username
                except:
                    approved_by='not-apporved'
                    
                vpp_table.append({'name':v.firstname+' '+v.lastname,'firstname':v.firstname,'approved_by':approved_by,'approved_by_id':v.approved_by,'lastname':v.lastname,'UID':v.UID,'id':v.id,'category':category,'comp':v.company_name,'exp_date':v.exp_date,'approved_date':v.approved_date,'vehicle_number':v.vehicle_number,'status':v.status,'mobile':v.mobile_number,'print_status':v.print_status,'print_count':v.print_count,'category_id':v.category_id,'created_at':v.reg_created_at,'remark':v.remark})
        
            data={'vpp_table':vpp_table,'role_id':int(request.session['user_role']),'user_id':int(request.session['user_id'])}
            html=render_to_string('tables/vapp_table.html',data)         
        
        
        return {'table_html':html}
    
    def update_front_page_in_ajax(request):
        
        table=request.POST.get('table')
        if int(table)==1:
            data=Tablepage.update_front_page(request,1)
        if int(table)==2:
            data=Tablepage.update_front_page(request,2)
        if int(table)==3:
            data=Tablepage.update_front_page(request,3)
        
        return JsonResponse(data)
        
    def update_bulk_print_page(request):
        table=request.POST.get('table')
        
        if request.session['user_role'] == 1:
            build_table_obj=Buildpass_table.objects.all().order_by('-id')
            event_table_obj=Eventpass_table.objects.all().order_by('-id')
            vapp_table_obj=Vapp_table.objects.all().order_by('-id')
        #ifomeuser
        if request.session['user_role'] == 2:
            build_table_obj=Buildpass_table.objects.all().order_by('-id')   
            event_table_obj=Eventpass_table.objects.all().order_by('-id')  
            vapp_table_obj=Vapp_table.objects.all().order_by('-id')
        htmls={}
        if int(table)==1:
            
            for i in request.session['build_id_array']:
                obj=build_table_obj.get(id=i)
                designation=build_designation.objects.get(id=obj.designation_id).designation
                try:
                    approved_by=user_DB.objects.get(id=obj.approved_by).username
                except:
                    approved_by='not-apporved'
                    
                data={ 'name':obj.firstname+' '+obj.lastname,'firstname':obj.firstname,'collected':obj.collected,'lastname':obj.lastname,'des_id':obj.designation_id,'id':obj.id,'UID':obj.UID,'designation':designation,'comp':obj.company_name,'exp_date':obj.exp_date,'status':obj.status,'print_status':obj.print_status,'print_count':obj.print_count,'other_des':obj.other_designation,'created_at':obj.reg_created_at,'remark':obj.remark,
                'role_id':int(request.session['user_role']),'categorys':vapp_category.objects.all(),'user_id':int(request.session['user_id'])}
                html=render_to_string('tables/table rows/build_table_row.html',data)  
                htmls[i]=html
        if int(table)==2:
            for i in request.session['event_id_array']:
                obj=event_table_obj.get(id=i)
                designation=eventpass_designation.objects.get(id=obj.designation_id).designation
                try:
                    approved_by=user_DB.objects.get(id=obj.approved_by).username
                except:
                    approved_by='not-apporved'
                m_data={'name':obj.firstname+' '+obj.lastname,'firstname':obj.firstname,'approved_by':approved_by,'approved_by_id':obj.approved_by,'collected':obj.collected,'lastname':obj.lastname,'des_id':obj.designation_id,'UID':obj.UID,'id':obj.id,'designation':designation,'comp':obj.company_name,'exp_date':obj.exp_date,'user_img':obj.file,'status':obj.status,'print_status':obj.print_status,'print_count':obj.print_count,'other_des':obj.other_designation,'created_at':obj.reg_created_at,'remark':obj.remark,'role_id':int(request.session['user_role']),'categorys':vapp_category.objects.all(),'user_id':int(request.session['user_id'])}
                html=render_to_string('tables/table rows/event_table_row.html',m_data)
                htmls[i]=html
        if int(table)==3:
            for i in request.session['vapp_id_array']:
                obj=vapp_table_obj.get(id=i)
                category=vapp_category.objects.get(id=obj.category_id).category
                try:
                    approved_by=user_DB.objects.get(id=obj.approved_by).username
                except:
                    approved_by='not-apporved'
                    
                data={'name':obj.firstname+' '+obj.lastname,'firstname':obj.firstname,'approved_by':approved_by,'approved_by_id':obj.approved_by,'collected':obj.collected,'lastname':obj.lastname,'UID':obj.UID,'id':obj.id,'category':category,'comp':obj.company_name,'exp_date':obj.exp_date,'approved_date':obj.approved_date,'vehicle_number':obj.vehicle_number,'status':obj.status,'mobile':obj.mobile_number,'print_status':obj.print_status,'print_count':obj.print_count,'category_id':obj.category_id,'created_at':obj.reg_created_at,'remark':obj.remark
                    ,'categorys':vapp_category.objects.all(),'role_id':int(request.session['user_role']),'user_id':int(request.session['user_id'])
                    }
                html=render_to_string('tables/table rows/vapp_table_row.html',data)        
                htmls[i]=html 
        return JsonResponse({'htmls':htmls})
        
    def get_new_data(request):
        
        
        speaker_reginstations_all=SpeakerRegistrations.objects.filter(deleted=0).all()
        invited_reginstations_all=InvitedRegistrations.objects.filter(deleted=0).all()
        applicant_reginstations_all=ApplicantRegistrations.objects.filter(deleted=0).all()
        desinguished_registrations_all=DistinguishedRegistrations.objects.filter(deleted=0).all()
        
        
        table=request.GET.get('table')
        
        build_new_data=False
        event_new_data=False
        vapp_new_data=False
        
        build_updated_id=[]
        event_updated_id=[]
        vapp_updated_id=[]
        build_new_html=[]
        event_new_html=[]
        vapp_new_html=[]
        
        build_last_row_id=0
        event_last_row_id=0
        vapp_last_row_id=0
        
        

      
        
        if int(table)==1 or int(table)==0:
            last_row_id=request.GET.get('build_last_row_id')
           
            last_obj=SpeakerRegistrations.objects.last()
            if int(last_obj.id) != int(last_row_id):
                new_data=speaker_reginstations_all.filter(id__range=(int(last_row_id)+1,last_obj.id))
                
                for i in new_data:
                    
                    obj=speaker_reginstations_all.get(id=i.id)
                    tr="<tr id='SP-"+str(i.id)+"'>"
                    
                    try:
                        approved_by=user_DB.objects.get(id=obj.approved_by).username
                    except:
                        approved_by='not-apporved'
                    data={'sp':obj,'approved_by_name':approved_by}
                    html=render_to_string('tables/table rows/speaker_table_row.html',data) 
                    new_html=tr+html+'</tr>'  
                    build_new_html.append(new_html)
                    
                build_new_data=True
                build_last_row_id=last_obj.id
            else:
                
                build_new_data=False

            updated_data=speaker_reginstations_all.filter(updated_at__range=[timezone.now()-timezone.timedelta(seconds=5),timezone.now()])
           
                
            for i in updated_data:
                
                obj=speaker_reginstations_all.get(id=i.id)
                tr="<tr id='SP-"+str(i.id)+"'>"
                # designation=build_designation.objects.get(id=obj.designation_id).designation
                try:
                    approved_by=user_DB.objects.get(id=obj.approved_by).username
                except:
                    approved_by='not-apporved'
                data={'sp':obj,'approved_by_name':approved_by}
                html=render_to_string('tables/table rows/speaker_table_row.html',data) 
                new_html=tr+html+'</tr>'  
                build_new_html.append(new_html)
                build_updated_id.append(i.id)
                build_new_data=True
                build_last_row_id=SpeakerRegistrations.objects.last().id
            
                
        if int(table)==2 or int(table)== 0:
            last_row_id=request.GET.get('build_last_row_id')
           
            last_obj=InvitedRegistrations.objects.last()
            if int(last_obj.id) != int(last_row_id):
                new_data=InvitedRegistrations.objects.filter(deleted=0,status=0).filter(id__range=(int(last_row_id)+1,last_obj.id)).filter(~Q(status=1))
                
                for i in new_data:
               
                    obj=invited_reginstations_all.get(id=i.id)
                    tr="<tr id='IN-"+str(i.id)+"'>"
                    
                    try:
                        approved_by=user_DB.objects.get(id=obj.approved_by).username
                    except:
                        approved_by='not-apporved'
                    data={'sp':obj,'approved_by_name':approved_by}
                    html=render_to_string('tables/table rows/invited_table_row.html',data) 
                    new_html=tr+html+'</tr>'  
                    build_new_html.append(new_html)
                    
                build_new_data=True
                build_last_row_id=last_obj.id
            else:
                
                build_new_data=False

            updated_data=invited_reginstations_all.filter(updated_at__range=[timezone.now()-timezone.timedelta(seconds=5),timezone.now()])
           
                
            for i in updated_data:
                
                obj=invited_reginstations_all.get(id=i.id)
                tr="<tr id='IN-"+str(i.id)+"'>"
                # designation=build_designation.objects.get(id=obj.designation_id).designation
                try:
                    approved_by=user_DB.objects.get(id=obj.approved_by).username
                except:
                    approved_by='not-apporved'
                data={'sp':obj,'approved_by_name':approved_by}
                html=render_to_string('tables/table rows/invited_table_row.html',data) 
                new_html=tr+html+'</tr>'  
                build_new_html.append(new_html)
                build_updated_id.append(i.id)
                build_new_data=True
                build_last_row_id=InvitedRegistrations.objects.last().id
                
                
        if int(table)==3 or int(table)== 0:
            last_row_id=request.GET.get('build_last_row_id')
           
            
            last_obj=ApplicantRegistrations.objects.last()
            
            if int(last_obj.id) != int(last_row_id):
                new_data=ApplicantRegistrations.objects.filter(deleted=0,status=0).filter(id__range=(int(last_row_id)+1,last_obj.id)).filter(~Q(status=1))
                
                for i in new_data:
               
                    obj=applicant_reginstations_all.get(id=i.id)
                    tr="<tr id='AP-"+str(i.id)+"'>"
                    
                    try:
                        approved_by=user_DB.objects.get(id=obj.approved_by).username
                    except:
                        approved_by='not-apporved'
                    data={'sp':obj,'approved_by_name':approved_by}
                    html=render_to_string('tables/table rows/applicant_table_row.html',data) 
                    new_html=tr+html+'</tr>'  
                    build_new_html.append(new_html)
                    
                build_new_data=True
                build_last_row_id=last_obj.id
            else:
                
                build_new_data=False

            updated_data=applicant_reginstations_all.filter(updated_at__range=[timezone.now()-timezone.timedelta(seconds=5),timezone.now()])
           
                
            for i in updated_data:
                
                obj=applicant_reginstations_all.get(id=i.id)
                tr="<tr id='AP-"+str(i.id)+"'>"
                # designation=build_designation.objects.get(id=obj.designation_id).designation
                try:
                    approved_by=user_DB.objects.get(id=obj.approved_by).username
                except:
                    approved_by='not-apporved'
                data={'sp':obj,'approved_by_name':approved_by}
                html=render_to_string('tables/table rows/applicant_table_row.html',data) 
                new_html=tr+html+'</tr>'  
                build_new_html.append(new_html)
                build_updated_id.append(i.id)
                build_new_data=True
                build_last_row_id=ApplicantRegistrations.objects.last().id
                
        if int(table)==4 or int(table)==0:
        
            last_row_id=request.GET.get('build_last_row_id')
           
            last_obj=DistinguishedRegistrations.objects.last()
            if int(last_obj.id) != int(last_row_id):
                new_data=desinguished_registrations_all.filter(id__range=(int(last_row_id)+1,last_obj.id))
                
                for i in new_data:
                    
                    obj=desinguished_registrations_all.get(id=i.id)
                    tr="<tr id='DG-"+str(i.id)+"'>"
                    
                    try:
                        approved_by=user_DB.objects.get(id=obj.approved_by).username
                    except:
                        approved_by='not-apporved'
                    data={'sp':obj,'approved_by_name':approved_by}
                    html=render_to_string('tables/table rows/distiguished_table_row.html',data) 
                    new_html=tr+html+'</tr>'  
                    build_new_html.append(new_html)
                    
                build_new_data=True
                build_last_row_id=last_obj.id
            else:
                
                build_new_data=False

            updated_data=desinguished_registrations_all.filter(updated_at__range=[timezone.now()-timezone.timedelta(seconds=5),timezone.now()])
           
                
            for i in updated_data:
                
                obj=desinguished_registrations_all.get(id=i.id)
                tr="<tr id='DG-"+str(i.id)+"'>"
                # designation=build_designation.objects.get(id=obj.designation_id).designation
                try:
                    approved_by=user_DB.objects.get(id=obj.approved_by).username
                except:
                    approved_by='not-apporved'
                data={'sp':obj,'approved_by_name':approved_by}
                html=render_to_string('tables/table rows/distiguished_table_row.html',data) 
                new_html=tr+html+'</tr>'  
                build_new_html.append(new_html)
                build_updated_id.append(i.id)
                build_new_data=True
                build_last_row_id=DistinguishedRegistrations.objects.last().id
                
        last_row={'build_row_id':build_last_row_id,'event_row_id':event_last_row_id,'vapp_row_id':vapp_last_row_id}
        new_html={'build_html':build_new_html,'event_html':event_new_html,'vapp_html':vapp_new_html,'build_updated_id':build_updated_id,'event_updated_id':event_updated_id,'vapp_updated_id':vapp_updated_id}
        new_data={'build_new_data':build_new_data,'event_new_data':event_new_data,'vapp_new_data':vapp_new_data}
        
        
        
        
        # user_activity_objects =0 OnlineUserActivity.get_user_activities()
        # number_of_active_users = user_activity_objects.count()

        online_list=Tablepage.user_online(request)
        
            
        return JsonResponse({'last_row_id':last_row,'new_data':new_data,'new_html':new_html,'online_list':online_list})        
    
    def user_online(request):
        
        user_username=request.user.username
        userdb=user_DB.objects.get(username=user_username)
        userdb.last_req_updated_time=timezone.localtime()
        userdb.is_online=1
        userdb.save()
        
        #get online users
        online_list=[]
        
        
        check_time=timezone.localtime()-timezone.timedelta(seconds=8)


        
        for u in user_DB.objects.filter(is_online=1).filter(~Q(id=userdb.id)):
           
           
            if u.last_req_updated_time < check_time:
                u.is_online=0
                u.save()
            else:
                online_list.append(u.username)
                
        return online_list     
    
    def undo_status(request):
        id=request.POST.get('id')
        table=request.POST.get('table')
        
        
        
        
        if int(table)==1:
            obj=SpeakerRegistrations.objects.get(id=id)
            obj.status=0
            obj.save()
            try:
                approved_by=user_DB.objects.get(id=obj.approved_by).username
            except:
                approved_by='not-apporved'
            data={'sp':obj,'approved_by_name':approved_by}
            html=render_to_string('tables/table rows/speaker_table_row.html',data)
            
            return JsonResponse({'table_html':html}) 
    
        if int(table)==2:
            obj=InvitedRegistrations.objects.get(id=id)
            obj.status=0
            obj.save()
            try:
                approved_by=user_DB.objects.get(id=obj.approved_by).username
            except:
                approved_by='not-apporved'
            data={'sp':obj,'approved_by_name':approved_by}
            html=render_to_string('tables/table rows/invited_table_row.html',data)
            return JsonResponse({'table_html':html}) 

        if int(table)==3:
            obj=ApplicantRegistrations.objects.get(id=id)
            obj.status=0
            obj.save()
            try:
                approved_by=user_DB.objects.get(id=obj.approved_by).username
            except:
                approved_by='not-apporved'
            data={'sp':obj,'approved_by_name':approved_by}
            html=render_to_string('tables/table rows/applicant_table_row.html',data)   
            return JsonResponse({'table_html':html}) 
            
        
    
    @login_required
    def create_unique(request):
       
        data={}
        new_count_html=''
        if request.GET.get('count') != None:
            count=request.GET.get('count')
            max_reg=request.GET.get('max_reg')
            sp_charset=request.GET.get('sp_charset')
            start=request.GET.get('start')
            unique=request.GET.get('unique_bool')
           
            for i in range(int(start),int(count)):
                
           
                obj=Unique_reg_code.objects.create(used=max_reg)
                
                
                if sp_charset != '':
                    obj.code=str( sp_charset + obj.code )
                    obj.save()
                
                if unique == 'false':
                    
                    if i <= 8:
                        code_num=str(0)+str(i + 1 )
                    else:
                        code_num=str(i + 1 )    
                    obj.code=str( sp_charset + code_num )
                    obj.save()
                code=str(obj.code)
                new_count_html+='<tr> <td>'+ code +' </td> </tr>'
                
            data['new_codes_tr']=new_count_html

            return JsonResponse(data)
        else:
            data['new_codes_tr']=new_count_html
            return render(request,'exstends/unique_code_generator.html',data)
    def show_delete(request):
        s_code=request.GET.get('s_code')
      
        results=Unique_reg_code.objects.filter(code__icontains=s_code).values_list('code',flat=True)
    
        return JsonResponse({'results':list(results)}) 
    def delete_codes(request):
        s_codes_array=request.POST.getlist('s_codes_array[]')
       
        obj=Unique_reg_code.objects.filter(code__in=s_codes_array)
        obj.delete()
        

        return JsonResponse({})
class Report():
    def report_page(request):
        build_designations=build_designation.objects.all()
        eventpass_designations=eventpass_designation.objects.all()
        vapp_designations=vapp_category.objects.all()
        
        data={'build_designations':build_designations,'eventpass_designations':eventpass_designations,'vapp_designations':vapp_designations}
        
            
        return render(request,'report.html',data)
    def getReportData(request):
     
        categorySel=request.GET.get('CategorySel')
        DesignationSel=request.GET.get('DesignationSel')
        DateFrom=request.GET.get('Datefrom')
        DateTo=request.GET.get('Dateto')
  
        if categorySel == '1':
            build_table=[] 
            build_table_obj=Buildpass_table.objects.filter(reg_created_at__range=[DateFrom,DateTo],designation_id=DesignationSel).order_by('-id')
            for b in build_table_obj:
                try:
                    approved_by=user_DB.objects.get(id=b.approved_by).username
                except:
                    approved_by='not-apporved'
                designation=build_designation.objects.get(id=b.designation_id).designation
                build_table.append({'name':b.firstname+' '+b.lastname,'collected': b.collected,'approved_by':approved_by,'approved_by_id':b.approved_by,'firstname':b.firstname,'lastname':b.lastname,'des_id':b.designation_id,'id':b.id,'UID':b.UID,'designation':designation,'comp':b.company_name,'exp_date':b.exp_date,'status':b.status,'print_status':b.print_status,'print_count':b.print_count,'other_des':b.other_designation,'created_at':b.reg_created_at,'remark':b.remark})
            
            data={'username':request.user.username,'build_table':build_table,'categorys':vapp_category.objects.all(),'build_pass_designations':build_designation.objects.all(),'event_pass_designations':eventpass_designation.objects.all()}
            Table_data = render_to_string('tables/report/rp_build_table.html',data)
        
        if categorySel == '2':
            event_table=[]
            event_table_obj=Eventpass_table.objects.filter(reg_created_at__range=[DateFrom,DateTo],designation_id=DesignationSel).order_by('-id')
            for e in event_table_obj[:100]:
                try:
                    approved_by=user_DB.objects.get(id=e.approved_by).username
                except:
                    approved_by='not-apporved'
                    
                designation=eventpass_designation.objects.get(id=e.designation_id).designation
                #img=eventpass_image_db.objects.get()
                event_table.append({'name':e.firstname+' '+e.lastname,'approved_by':approved_by,'approved_by_id':e.approved_by,'firstname':e.firstname,'collected':e.collected,'lastname':e.lastname,'des_id':e.designation_id,'UID':e.UID,'id':e.id,'designation':designation,'comp':e.company_name,'exp_date':e.exp_date,'user_img':e.file,'status':e.status,'print_status':e.print_status,'print_count':e.print_count,'other_des':e.other_designation,'created_at':e.reg_created_at,'id_proof':e.id_proof,'remark':e.remark})
    
            data={'username':request.user.username,'event_table':event_table}
            Table_data = render_to_string('tables/report/rp_event_table.html',data)
        
        if categorySel == '3':
            vpp_table=[]
            vapp_table_obj=Vapp_table.objects.filter(reg_created_at__range=[DateFrom,DateTo],category_id=DesignationSel).order_by('-id')
            for v in vapp_table_obj[:100]:
                try:
                    approved_by=user_DB.objects.get(id=v.approved_by).username
                except:
                    approved_by='not-apporved'
                category=vapp_category.objects.get(id=v.category_id).category
                vpp_table.append({'name':v.firstname+' '+v.lastname,'firstname':v.firstname,'approved_by':approved_by,'approved_by_id':v.approved_by,'collected': v.collected,'lastname':v.lastname,'UID':v.UID,'id':v.id,'category':category,'comp':v.company_name,'exp_date':v.exp_date,'approved_date':v.approved_date,'vehicle_number':v.vehicle_number,'status':v.status,'mobile':v.mobile_number,'print_status':v.print_status,'print_count':v.print_count,'category_id':v.category_id,'created_at':v.reg_created_at,'remark':v.remark})    
            
            data={'username':request.user.username,'vpp_table':vpp_table}
            Table_data = render_to_string('tables/report/rp_vapp_table.html',data)
        return JsonResponse({'Table':Table_data})



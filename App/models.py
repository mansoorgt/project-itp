from django.db import models
import uuid
# Create your models here.

def speaker_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    print(instance)
    return 'speakerReginstration/{0}/{1}'.format(instance.mobile, filename)

def invited_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    print(instance)
    return 'invitedReginstration/{0}/{1}'.format(instance.mobile, filename)
def applicant_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    print(instance)
    return 'ApplicantReginstration/{0}/{1}'.format(instance.mobile, filename)

class SpeakerRegistrations(models.Model):
    first_name=models.TextField(max_length=200,null=True)
    last_name=models.TextField(max_length=200,null=True)
    designation=models.TextField(max_length=200,null=True)
    company=models.TextField(max_length=200,null=True)
    email=models.TextField(max_length=200,null=True)
    mobile=models.TextField(max_length=200,null=True)
    country=models.TextField(max_length=200,null=True)
    traveling_from=models.TextField(max_length=200,null=True)
    retun_date_time=models.DateTimeField(null=True)
    depature_date_time=models.DateTimeField(null=True)
    outline_talk=models.TextField(max_length=200,null=True)
    passport_copy=models.FileField(upload_to=speaker_directory_path)
    photo_upload=models.FileField(upload_to=speaker_directory_path)
    ksa_visa=models.IntegerField(null=True)
    
    status=models.IntegerField(null=True)
    created_at=models.DateTimeField(null=True)
    updated_at=models.DateTimeField(null=True)
    approved_by=models.IntegerField(null=True)
    collected=models.IntegerField(null=True)
    print_status=models.IntegerField(null=True)
    remark=models.TextField(default='',null=True)
    
    deleted=models.IntegerField(default=0)
    class Meta:
        db_table='app_speakerregistrations'
        
class InvitedRegistrations(models.Model):
    first_name=models.TextField(max_length=200,null=True)
    last_name=models.TextField(max_length=200,null=True)
    designation=models.TextField(max_length=200,null=True)
    company=models.TextField(max_length=200,null=True)
    email=models.TextField(max_length=200,null=True)
    mobile=models.TextField(max_length=200,null=True)
    country=models.TextField(max_length=200,null=True)
    occupation=models.IntegerField(null=True)
    intrested_in=models.CharField( max_length=200,null=True)
    pre_attend=models.IntegerField(null=True)
    urc_code=models.CharField( max_length=200,null=True)
    passport_copy=models.FileField(upload_to=invited_directory_path)
    photo_upload=models.FileField(upload_to=invited_directory_path)
    ksa_visa=models.IntegerField(null=True)
    
    status=models.IntegerField(null=True)
    created_at=models.DateTimeField(null=True)
    updated_at=models.DateTimeField(null=True)
    approved_by=models.IntegerField(null=True)
    collected=models.IntegerField(null=True)
    print_status=models.IntegerField(null=True)
    remark=models.TextField(default='',null=True)
    
    deleted=models.IntegerField(default=0)
    class Meta:
        db_table='app_invitedregistrations'
        
class ApplicantRegistrations(models.Model):
    first_name=models.TextField(max_length=200,null=True)
    last_name=models.TextField(max_length=200,null=True)
    designation=models.TextField(max_length=200,null=True)
    company=models.TextField(max_length=200,null=True)
    email=models.TextField(max_length=200,null=True)
    mobile=models.TextField(max_length=200,null=True)
    country=models.TextField(max_length=200,null=True)
    pre_attend=models.IntegerField(null=True)
    
    occupation=models.IntegerField(null=True)
    intrested_in=models.CharField( max_length=200,null=True)
    
    passport_copy=models.FileField(upload_to=applicant_directory_path)
    photo_upload=models.FileField(upload_to=applicant_directory_path)
    ksa_visa=models.IntegerField(null=True)
    
    status=models.IntegerField(null=True)
    created_at=models.DateTimeField(null=True)
    updated_at=models.DateTimeField(null=True)
    approved_by=models.IntegerField(null=True)
    collected=models.IntegerField(null=True)
    print_status=models.IntegerField(null=True)
    remark=models.TextField(default='',null=True)
    
    deleted=models.IntegerField(default=0)
    class Meta:
        db_table='app_applicantregistrations'
        
        
class occupations(models.Model):
    occupation_name=models.TextField(null=True,max_length=200)
    status=models.IntegerField(default=1)
    class Meta:
        db_table='app_occupations'
#permisisons

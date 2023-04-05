
import os
from unicodedata import category, name
from django.db import models

# Create your models here.


#user 
class user_DB(models.Model):
    username=models.CharField(max_length=200,null=True,blank=False)
    role=models.IntegerField(null=True,blank=False)
    is_online=models.IntegerField(null=True,blank=False)
    last_req_updated_time=models.DateTimeField(null=True,blank=False)
    class Meta:
        db_table='webapp_user_db'
#build_pass dbs
class Buildpass_table(models.Model):
    firstname=models.CharField(max_length=200,null=True,blank=False)
    lastname=models.CharField(max_length=200,null=True,blank=False)
    mobile=models.CharField(max_length=200,null=True,blank=False)
    email=models.CharField(max_length=200,null=True,blank=False)
    designation_id=models.IntegerField(null=True,blank=False)
    company_name=models.CharField(max_length=200,null=True,blank=False)
    event_pass=models.BooleanField(default=True)
    exp_date=models.DateField(null=True,blank=False)
    reg_created_at=models.DateTimeField(auto_now_add=True)
    UID=models.CharField(max_length=200,null=True,blank=False)
    print_status=models.IntegerField(null=True,blank=False)
    print_count=models.IntegerField(null=True,blank=False)
    status=models.IntegerField(null=True,blank=False)
    other_designation=models.CharField(max_length=200,null=True,blank=False)
    remark=models.CharField(max_length=200,null=True,blank=False)
    updated_at=models.DateTimeField(null=True,blank=False)
    collected=models.IntegerField(null=True,blank=False)
    approved_by=models.IntegerField(null=True,blank=False)
    def __str__(self):
         return self.firstname
    class Meta:
        db_table='webapp_buildpass_table'
        
class build_designation(models.Model):
    designation=models.CharField(max_length=200,null=True,blank=False)
    class Meta:
        db_table='webapp_build_designation'

#event_pass dbs
class Eventpass_table(models.Model):
    firstname=models.CharField(max_length=200,null=True,blank=False)
    lastname=models.CharField(max_length=200,null=True,blank=False)
    mobile=models.CharField(max_length=200,null=True,blank=False)
    email=models.CharField(max_length=200,null=True,blank=False)
    designation_id=models.IntegerField(null=True,blank=False)
    company_name=models.CharField(max_length=200,null=True,blank=False)
    exp_date=models.DateField(null=True,blank=False)
    reg_created_at=models.DateTimeField(auto_now_add=True)
    file=models.FileField(upload_to='media/event_pass/profile', max_length=100,null=True) 
    id_proof_img=models.FileField(upload_to='media/event_pass/idproof', max_length=100,null=True) 
    id_proof_back_img=models.FileField(upload_to='media/event_pass/idproof', max_length=100,null=True) 
    UID=models.CharField(max_length=200,null=True,blank=False)
    print_status=models.IntegerField(null=True,blank=False)
    print_count=models.IntegerField(null=True,blank=False)
    nationality=models.CharField(max_length=200,null=True,blank=False)
    id_proof_cat=models.IntegerField(null=True,blank=False)
    id_proof=models.CharField(max_length=200,null=True,blank=False)
    status=models.IntegerField(null=True,blank=False)
    other_designation=models.CharField(max_length=200,null=True,blank=False)
    remark=models.CharField(max_length=200,null=True,blank=False)
    updated_at=models.DateTimeField(null=True,blank=False)
    collected=models.IntegerField(null=True,blank=False)
    approved_by=models.IntegerField(null=True,blank=False)
    def __str__(self):
         return self.firstname
    class Meta:
        db_table='webapp_eventpass_table'
class eventpass_image_db(models.Model):
    pass_id=models.IntegerField(null=True,blank=False)
    class Meta:
        db_table='webapp_eventpass_image_db'
    
class eventpass_designation(models.Model):
    designation=models.CharField(max_length=200,null=True,blank=False)
    class Meta:
        db_table='webapp_eventpass_designation'

        
#vapp_pass db       
class Vapp_table(models.Model):
    firstname=models.CharField(max_length=200,null=True,blank=False)
    lastname=models.CharField(max_length=200,null=True,blank=False)
    email=models.CharField(max_length=200,null=True,blank=False)
    vehicle_number=models.CharField(max_length=200,null=True,blank=False)
    mobile_number=models.CharField(max_length=200,null=True,blank=False)
    company_name=models.CharField(max_length=200,null=True,blank=False)
    category_id=models.IntegerField(null=True,blank=False)
    exp_date=models.DateField(null=True,blank=False)
    reg_created_at=models.DateTimeField(auto_now_add=True)
    UID=models.CharField(max_length=200,null=True,blank=False)
    print_status=models.IntegerField(null=True,blank=False)
    print_count=models.IntegerField(null=True,blank=False)
    status=models.IntegerField(null=True,blank=False)
    approved_date=models.DateField(null=True,blank=False)
    remark=models.CharField(max_length=200,null=True,blank=False)
    mulkya=models.FileField(upload_to='media/vapp/mulkya', max_length=100,null=True)
    emirates_id=models.FileField(upload_to='media/vapp/emirates_id', max_length=100,null=True)
    emirates_id_back=models.FileField(upload_to='media/vapp/emirates_id', max_length=100,null=True)
    vehicle_type_id=models.IntegerField(null=True,blank=False)
    updated_at=models.DateTimeField(null=True,blank=False)
    collected=models.IntegerField(null=True,blank=False)
    approved_by=models.IntegerField(null=True,blank=False)
    def __str__(self):
         return self.firstname
    class Meta:
        db_table='webapp_vapp_table'
class vapp_vehicle_type(models.Model):
    type=models.CharField(max_length=200,null=True,blank=False)
    def __str__(self):
         return self.type
    class Meta:
        db_table='vapp_vehicle_type'
class vapp_category(models.Model):
    category=models.CharField(max_length=200,null=True,blank=False)
    class Meta:
        db_table='webapp_vapp_category'
#permisisons
   
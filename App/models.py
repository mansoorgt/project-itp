from django.db import models

# Create your models here.

def speaker_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    print(instance)
    return 'speakerReginstration/{0}/{1}'.format(instance.mobile, filename)

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
    class Meta:
        db_table='app_speakerregistrations'
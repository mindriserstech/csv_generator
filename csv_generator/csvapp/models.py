from datetime import datetime
from django.db import models
from django.forms import CharField, PasswordInput
# Create your models here.
class UserType(models.Model):
    usertype = models.CharField(max_length=100)
    status = models.BooleanField(True)

    class Meta:
        db_table = "csv_usertypes"

class CsvUserType(models.Model):
    usertype = models.CharField(max_length=100)
    status = models.BooleanField(True)

    class Meta:
        db_table = "csvusertypes"


#  our application model
class CsvUser(models.Model):
    first_name = models.CharField(max_length=100, null=False)
    middle_name = models.CharField(max_length=100, null=True)
    last_name = models.CharField(max_length=100, null=False)
    contact = models.CharField(max_length=20, null=True)
    email = models.EmailField(unique=True, null=False)
    username = models.CharField(max_length=100,unique=True, null=False)
    password = models.CharField(max_length=100, null=False)
    verification_code = models.CharField(max_length=20, null=False)
    is_verified = models.BooleanField(default=False)
    is_active = models.BooleanField(null=False, default=1)
    created_at = models.DateTimeField(null=False)

    class Meta:
        db_table = "csv_user"

    # converting user object to string 
    def __str__(self):
        return self.first_name



class CsvUserProfile(models.Model):
    profile_url = models.FileField(upload_to='users/profile/')
    user_email = models.CharField(max_length=200)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        db_table = "csv_user_profile"

    def __str__(self):
        return self.profile_url

class CsvUserSchedule(models.Model):
    title = models.CharField(max_length=50, null=False)
    description = models.CharField(max_length=200, null=False)
    schedule_time = models.DateTimeField(null=False)
    set_alarm = models.DateTimeField(null=False)
    venue = models.CharField(max_length=100, null=True)
    event_type = models.CharField(max_length=100, null=True)
    priority = models.CharField(max_length=100, null=False)
    created_at = models.DateTimeField(null=False, default=datetime)
    status = models.BooleanField(default=True)
    user_id = models.BigIntegerField(null=True)

    class Meta:
        db_table = "csv_userschedule"



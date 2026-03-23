from django.db import models
from django.contrib.auth.models import AbstractUser,PermissionsMixin
import uuid
from django.contrib.auth.models import BaseUserManager
# Create your models here.

# user manager
class UserManager(BaseUserManager):
    def create_user(self,email,username,password=None , **extra_fields):
        if not email:
            return ValueError('Users must have an email address')   
        email = self.normalize_email(email)
        user = self.model(email=email,username=username, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self,email,username,password=None,**extra_fields):
        extra_fields.setdefault('is_staff',True)
        extra_fields.setdefault('is_superuser',True)
        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')
        
        return self.create_user(email,username,password,**extra_fields)

# user model
class User(AbstractUser,PermissionsMixin):
    # core identity
    id=models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    email = models.EmailField(unique=True,blank=False,null=False)
    username = models.CharField(max_length=30, unique=True)
    password = models.CharField(max_length=128,blank=False,null=False)
    
    # profile
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=30,blank=True)
    profile_image = models.ImageField(upload_to='profiles/',blank=True,null=True)
    phone_number = models.CharField(max_length=15,blank=True,null=True)
    
    # roles
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
    
    # task related stats
    total_tasks_created = models.IntegerField(default=0)
    total_tasks_completed = models.IntegerField(default=0)
    total_tasks_failed = models.IntegerField(default=0)
    current_running_tasks = models.IntegerField(default=0)
    
    # rate limmiting
    max_concurrent_tasks = models.IntegerField(default=5)
    daily_task_limit = models.IntegerField(default=10)
    task_used_today = models.IntegerField(default=0)
    
    # subscriptions
    plan_choice = (
        ('free','free'),
        ('premium','premium')
    )
    
    plan = models.CharField(max_length=10,choices=plan_choice,default='free')
    
    # time fields
    date_joined = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now=True)
    
    # manager
    objects = UserManager()
    # fields for superuser
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
    
    def __str__(self):
        return self.username


    def __str__(self):
        return self.email
    


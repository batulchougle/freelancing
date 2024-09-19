from django.db import models

# Create your models here.
from django.db import models
from django.utils.translation import gettext_lazy as _
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from .manager import UserManager
from django.conf import settings

# Create your models here.
class Institute(AbstractBaseUser):
    name = models.CharField(max_length=255, unique=True)
    email = models.EmailField(unique=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_verified=models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    USERNAME_FIELD="email"
    REQUIRED_FIELDS=["name"]
    objects=UserManager()
    def __str__(self):
        return self.name
    
class Student(AbstractBaseUser,PermissionsMixin):
    id = models.BigAutoField(primary_key=True, editable=False)
    institute = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_verified=models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now=True)

    USERNAME_FIELD="email"

    REQUIRED_FIELDS=["name","username"]
    objects=UserManager()


    def __str__(self):
        return self.email
    
    @property
    def get_name(self):
        return (self.name)
    @property
    def get_username(self): 
        return (self.username)
    @property
    def get_name(self):
        return (self.name)
    

    groups = models.ManyToManyField(
        'auth.Group',
        related_name='student_groups',  # Unique related_name
        blank=True,
        verbose_name=_('groups')
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='student_permissions',  # Unique related_name
        blank=True,
        verbose_name=_('user permissions')
    )

     
     
     
     

    

class Faculty(AbstractBaseUser,PermissionsMixin):
    id = models.BigAutoField(primary_key=True, editable=False)
    institute = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_verified=models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now=True)

    USERNAME_FIELD="email"

    REQUIRED_FIELDS=["name","username"]
    
    objects=UserManager()

    def __str__(self):
        return self.email
    
    @property
    def get_name(self):
        return (self.name)
    @property
    def get_username(self): 
        return (self.username)
    @property
    def get_name(self):
        return (self.name)
    

    groups = models.ManyToManyField(
        'auth.Group',
        related_name='faculty_groups',  # Unique related_name
        blank=True,
        verbose_name=_('groups')
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='faculty_permissions',  # Unique related_name
        blank=True,
        verbose_name=_('user permissions')
    )

class OneTimePassword(models.Model):
    user=models.OneToOneField(Institute, on_delete=models.CASCADE)
    code=models.CharField(max_length=6, unique=True)

    def __str__(self):
        return f"{self.user.name}-passcode"        
    

    
   
    
    

    


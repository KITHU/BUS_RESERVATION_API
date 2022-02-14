from django.db import models
from django.db.models.deletion import DO_NOTHING
from rest_framework_simplejwt.tokens import RefreshToken 
from django.contrib.auth.models import (
    AbstractBaseUser, BaseUserManager, 
    PermissionsMixin)


class UserManager(BaseUserManager):

    def create_user(self, username, email, password=None, **kwargs):
        if username is None:
            raise TypeError("Users should have a username")
        if email is None:
            raise TypeError("Users should have email")
        user=self.model(username=username, email=self.normalize_email(email))
        user.set_password(password)
        user.role= kwargs.get('role', 2)
        user.save()
        return user


    def create_superuser(self, username, email, password=None):
        if password is None:
            raise TypeError("Users should have a password")
        
        user=self.create_user(username, email, password)
        user.is_superuser = True
        user.is_staff = True
        user.role = 1
        user.save()
        return user


class User(AbstractBaseUser, PermissionsMixin):
    ADMIN = 1
    MANAGER = 2
    CASHIER = 3

    ROLE_CHOICES = (
        (ADMIN, 'Admin'),
        (MANAGER, 'Manager'),
        (CASHIER, 'Cashier')
    )
    username = models.CharField(max_length=50, unique=True , db_index=True)
    email = models.EmailField(max_length=80, unique=True, db_index=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    role = models.PositiveSmallIntegerField(choices=ROLE_CHOICES, blank=True, null=True, default=3)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
  

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
    
    objects = UserManager()

    def __str__(self):
        return self.email

    def tokens(self):
        refresh = RefreshToken.for_user(self)
        return {
            'refresh':str(refresh),
            'access':str(refresh.access_token)
        }

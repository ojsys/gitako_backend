from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models

class FarmerManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(email, password, **extra_fields)

class Farmer(AbstractBaseUser):

    GENDER_CHOICES = [
        ('Select Gender', 'Select Gender'),
        ('Male', 'Male'),
        ('Female', 'Female'),
        
    ]

    email = models.EmailField(unique=True)
    full_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=10)
    gender = models.CharField(max_length=15, choices=GENDER_CHOICES)
    age = models.IntegerField()
    address = models.TextField()
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    farm_name = models.CharField(max_length=100)
    registration_date = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    password = models.CharField(max_length=100)

    objects = FarmerManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['full_name', 'age', 'phone_number', 'gender', 'address', 'city', 'state', 'farm_name']

    class Meta:
        verbose_name = 'Farmer'
        verbose_name_plural = 'Farmers'


    def __str__(self):
        return self.full_name
    
    






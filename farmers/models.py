from django.db import models

class Farmer(models.Model):

    GENDER_CHOICES = [
        ('Select Gender', 'Select Gender'),
        ('Male', 'Male'),
        ('Female', 'Female'),
        
    ]

    full_name = models.CharField(max_length=100)
    age = models.IntegerField()
    email = models.EmailField()
    phone_number = models.CharField(max_length=10)
    gender = models.CharField(max_length=15, choices=GENDER_CHOICES)
    address = models.TextField()
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    farm_name = models.CharField(max_length=100)
    registration_date = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.full_name
    
    def verbose_name_plural(self):
        return "Farmers"
    



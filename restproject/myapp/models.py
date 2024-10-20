from django.db import models

# Create your models here.
class UserProfile(models.Model):
    first_name = models.CharField(max_length=50)  
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True) 
    password = models.CharField(max_length=128)  
    age = models.IntegerField(null=True, blank=True)  
    date_of_birth = models.DateField(null=True, blank=True)  
    profile_image = models.ImageField(upload_to='profile_images/', null=True, blank=True) 
    bio = models.TextField(null=True, blank=True)  

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
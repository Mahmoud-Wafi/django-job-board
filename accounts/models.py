from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from phonenumber_field.modelfields import PhoneNumberField
# Create your models here.
class City(models.Model):
    name= models.CharField(max_length=30)
    
    
    def __str__(self) -> str:
        return self.name
    
    
class Profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    city=models.ForeignKey('City' , related_name='user_city', on_delete= models.CASCADE,blank=True, null=True)
    phone_number = PhoneNumberField(blank=True, null=True)
    image= models.ImageField(upload_to='profile/')
    
    def __str__(self) -> str:
         return self.user.username
    
    
    
@receiver(post_save , sender=User) 
def create_user_profile(sender,instance,created,**kwargs):
    if created:
        Profile.objects.create(user=instance)
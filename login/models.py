from django.db import models

# Create your models here.
class sellproduct(models.Model):
    name=models.CharField(max_length=100,default='Enter your name')
    product=models.CharField(max_length=100,default='What do you want to sell')
    cost=models.IntegerField()
    image=models.ImageField(null=True,blank=True,upload_to='images/')
    issold=models.BooleanField(default=True)
    phonenumber=models.TextField(max_length=20,default='00000000000')
    

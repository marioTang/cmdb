from django.db import models

# Create your models here.
class sysmsg(models.Model):
    biosversion=models.CharField(max_length=30)
    kernelrelease=models.CharField(max_length=30)
    os=models.CharField(max_length=30)
    cpu_model=models.CharField(max_length=30)
    host=models.CharField(max_length=30)
    ip_interfaces=models.CharField(max_length=30)

class user(models.Model):
    username=models.CharField(max_length=20)
    password=models.CharField(max_length=30)
    email=models.CharField(max_length=32)
    telephone = models.CharField(max_length=32)
    c_time=models.DateTimeField(auto_now_add=True)



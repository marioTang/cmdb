from django.db import models

# Create your models here.
class systemmsg(models.Model):
    osfinger=models.CharField(max_length=30)
    osarch=models.CharField(max_length=30)
    kernelrelease=models.CharField(max_length=30)
    cpu_model=models.CharField(max_length=40)
    num_cpus=models.CharField(max_length=30)
    mac_interfaces=models.CharField(max_length=30)
    hostname=models.CharField(max_length=30)
    masterip=models.CharField(max_length=30)
    nameid=models.CharField(max_length=30)

class miniondata(models.Model):
    SwapTotal = models.DecimalField(max_digits=19, decimal_places=2)
    SwapFree = models.DecimalField(max_digits=19, decimal_places=2)
    MemFree = models.DecimalField(max_digits=19, decimal_places=2)
    MemTotal = models.DecimalField(max_digits=19, decimal_places=2)
    grading_size = models.DecimalField(max_digits=19, decimal_places=2)
    boot_size = models.DecimalField(max_digits=19, decimal_places=2)
    home_szie = models.DecimalField(max_digits=19, decimal_places=2)
    swaptmp_szie = models.DecimalField(max_digits=19, decimal_places=2)
    gen_available = models.DecimalField(max_digits=19, decimal_places=2)
    boot_available = models.DecimalField(max_digits=19, decimal_places=2)
    home_available = models.DecimalField(max_digits=19, decimal_places=2)
    swaptmp_available = models.DecimalField(max_digits=19, decimal_places=2)
    cpulod15_min = models.DecimalField(max_digits=19, decimal_places=2)
    cpulod5_min = models.DecimalField(max_digits=19, decimal_places=2)
    cpulod1_min = models.DecimalField(max_digits=19, decimal_places=2)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)













from django.db import models
from django.contrib.auth.models import Permission, User
from django.contrib.contenttypes.models import ContentType
from django.shortcuts import get_object_or_404
from playsound import playsound

# Create your models here.
class Plant(models.Model):
    #plant_id = models.OneToOneField(Dataplant, on_delete=models.DO_NOTHING)
    plant_name = models.CharField(max_length=100)
    plant_hum = models.DecimalField(max_digits=10, decimal_places=2)
    plant_temp = models.DecimalField(max_digits=10, decimal_places=2)
    plant_hi = models.DecimalField(max_digits=10, decimal_places=2)
    plant_light = models.DecimalField(max_digits=10, decimal_places=2)
    plant_status = models.CharField(max_length=100)
    foto = models.CharField(max_length=100)
    
    def __str__(self):
        return self.plant_name

class Dataplant(models.Model):
    dataplant_id = models.AutoField(primary_key=True)
    dataplant_date = models.DateTimeField(auto_now=True)
    plant_id = models.CharField(max_length=100)
    plant_hum = models.DecimalField(max_digits=10, decimal_places=2)
    plant_temp = models.DecimalField(max_digits=10, decimal_places=2)
    plant_hi = models.DecimalField(max_digits=10, decimal_places=2)
    plant_light = models.DecimalField(max_digits=10, decimal_places=2)
    plant_status = models.CharField(max_length=100)
    
    def __str__(self):
        return self.plant_id



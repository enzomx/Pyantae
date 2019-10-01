from django.db import models



# Create your models here.
class Plant(models.Model):
    plant_name = models.CharField(max_length=100)
    plant_hum = models.DecimalField(max_digits=10, decimal_places=2)
    plant_temp = models.DecimalField(max_digits=10, decimal_places=2)
    plant_hi = models.DecimalField(max_digits=10, decimal_places=2)
    plant_light = models.DecimalField(max_digits=10, decimal_places=2)
    plant_status = models.CharField(max_length=100)
    foto = models.CharField(max_length=100)
    
    def __str__(self):
        return self.plant_name

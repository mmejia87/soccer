from django.db import models

# Create your models here.
class Selecciones(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)

class Grupos(models.Model):
    seccion = models.CharField(max_length=100)
    equipos = models.CharField(max_length=100)
    
    

from django.db import models
 
class Cliente(models.Model):
    nombre = models.CharField("Nombre", max_length=200)
    identificacion = models.CharField("Identificación", max_length=50, unique=True)
    regimen_tributario = models.CharField("Regimen Tributario", max_length=100)
    direccion = models.CharField("Dirección", max_length=200)
    email = models.EmailField("Email")
    telefono = models.CharField("Teléfono", max_length=20)
 
    def __str__(self):
        return self.nombre
 
# Create your models here.
from typing import ClassVar
from django.db import models
from django.db.models.fields import CharField

# Create your models here.

class DatosColaboradores(models.Model):
    rut = models.CharField(primary_key=True,max_length=10,verbose_name='RUT Colaborador')
    nombre = models.CharField(max_length=100,verbose_name='Nombre Colaborador')
    telefono = models.CharField(max_length=9,verbose_name='Telefono Colaborador')
    dir = models.CharField(max_length=100,verbose_name='Dirección Colaborador')
    email = models.EmailField(verbose_name='Correo Colaborador')
    pais = models.CharField(max_length=30,verbose_name='País Colaborador')
    clave = models.CharField(max_length=50,verbose_name='Contraseña')
    imagen = models.ImageField(upload_to='colaboradores/',null=False,blank=True)

    def __str__(self):
       return self.name
   
   
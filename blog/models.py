from django.db import models
from django.core.validators import MinValueValidator
from django.db.models import Sum,Count
from django.contrib.auth.models import BaseUserManager, AbstractUser
from django.contrib.auth.models import User
import django
from django.conf import settings

# Create your models here.

class Region(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre

class Ciudad(models.Model):
    region = models.ForeignKey(Region,on_delete=models.CASCADE)
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre

class Tienda(models.Model):
    nombre = models.CharField(max_length=30, blank=False,unique=True)
    sucursal = models.CharField(max_length=30)
    direccion = models.CharField(max_length=30, blank=False)
    region = models.ForeignKey(Region,related_name='regi', on_delete=models.SET_NULL, null=True)
    ciudad = models.ForeignKey(Ciudad,related_name='city', on_delete=models.SET_NULL, null=True)
    estado_choices = (
        ('PENDIENTE', 'Pendiente'),
        ('APROBADO', 'Aprobado'),
    )
    estado = models.CharField(max_length=30, choices=estado_choices, default='PENDIENTE')

    def publish(self):
        self.save()

    def __str__(self):
        return self.nombre
    

class Lista(models.Model):
    nombre = models.CharField(max_length=30, blank=False,default='')
    totalAgregados = models.IntegerField(validators=[MinValueValidator(1)],default=0)
    totalComprados = models.IntegerField(validators=[MinValueValidator(1)],default=0)
    costoReal =  models.IntegerField(validators=[MinValueValidator(1)],default=0)
    costoPresupuestado = models.IntegerField(validators=[MinValueValidator(1)],default=0)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)


    def __str__(self):
        return self.nombre

    def publish(self):
        
        self.save()


class Producto(models.Model):
    
    nombre = models.CharField(max_length=30, blank=False)
    costoPresupuestado = models.IntegerField(validators=[MinValueValidator(1)],default=0)
    costoReal = models.IntegerField(validators=[MinValueValidator(1)],default=0)
    notasAdicionales = models.CharField(max_length=50)
    estado_choices = (
        ('COMPRADO', 'Comprado'),
        ('PENDIENTE', 'Pendiente'),
    )
    estado = models.CharField(max_length=30, choices=estado_choices, default='PENDIENTE')
    tienda = models.ForeignKey(Tienda, on_delete=models.SET_NULL, null=True ,related_name='est',limit_choices_to={'estado': 'APROBADO'})
    lista = models.ForeignKey(Lista, on_delete=models.SET_NULL, null=True)

    def publish(self):
        self.save()

    def __str__(self):
        return self.nombre

    def getestado(self):
        return self.tienda.estado




   

   


    


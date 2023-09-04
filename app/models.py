from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Prenda(models.Model):
    tipoPrenda = models.CharField(max_length=15, blank=False)
    tela = models.CharField(max_length=20, blank=False)
    color = models.CharField(max_length=20, blank=False)
    talla = models.CharField(max_length=2, blank=False)
    precio = models.DecimalField(max_digits=10, decimal_places=2, blank=False)
    cantidad = models.IntegerField(blank=False)
    descripcion = models.CharField(max_length=240, blank=False)
    telefonoVendedor = models.IntegerField()
    emailVendedor = models.EmailField()
    imagenPrenda = models.ImageField(upload_to='imagenes/', null=True, blank=False)

class Calzado(models.Model):
    tipoCalzado = models.CharField(max_length=15, blank=False)
    color = models.CharField(max_length=20, blank=False)
    talla = models.CharField(max_length=2, blank=False)
    precio = models.DecimalField(max_digits=10, decimal_places=2, blank=False)
    cantidad = models.IntegerField(blank=False)
    descripcion = models.CharField(max_length=240, blank=False)
    telefonoVendedor = models.IntegerField()
    emailVendedor = models.EmailField()    
    imagenCalzado = models.ImageField(upload_to='imagenes/', null=True, blank=False)

class Accesorio(models.Model):
    tipoAccesorio = models.CharField(max_length=15, blank=False)
    material = models.CharField(max_length=20, blank=False)
    precio = models.DecimalField(max_digits=10, decimal_places=2, blank=False)
    size = models.CharField(max_length=10, blank=False)
    cantidad = models.IntegerField(blank=False)
    descripcion = models.CharField(max_length=240, blank=False)
    telefonoVendedor = models.IntegerField()
    emailVendedor = models.EmailField()    
    imagenAccesorio = models.ImageField(upload_to='imagenes/', null=True, blank=False)

class EventosBazaar(models.Model):
    ciudad = models.CharField(max_length=40, blank=False)
    direccion = models.CharField(max_length=50, blank=False)
    fecha = models.DateField(blank=False)
    horario = models.CharField(max_length=30, blank=False)
    descripcion = models.CharField(max_length=240, blank=False)
    
class Avatar(models.Model):
    imagen = models.ImageField(upload_to="avatares")
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user} {self.imagen}"
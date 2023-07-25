from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class CategoriaProducto(models.Model):
    nombre=models.CharField(max_length=50)
    created=models.DateField(auto_now_add=True)
    update=models.DateField(auto_now_add=True)

    
    class Meta:
        verbose_name='categoriaProducto'
        verbose_name_plural='categoriasProducto'

    def __str__(self):
        return self.nombre
    

class Producto(models.Model):  
    nombre=models.CharField(max_length=50)
    categorias=models.ForeignKey(CategoriaProducto, on_delete=models.CASCADE)
    imagen=models.ImageField(upload_to='tienda', null=True, blank=True)
    Precio=models.FloatField()
    disponibilidad=models.BooleanField(default=True)


    class Meta:
        verbose_name='Producto'
        verbose_name_plural='Productos'


    
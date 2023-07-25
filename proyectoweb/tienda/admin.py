from django.contrib import admin
from .models import CategoriaProducto,Producto
# Register your models here.


class CategoriaProdAdmin(admin.ModelAdmin):
    readonly_fields=('created','update')


class ProductoAdmin(admin.ModelAdmin):
    readonly_fields=('created','update')

admin.site.register(CategoriaProducto, CategoriaProdAdmin)

admin.site.register(Producto, ProductoAdmin)

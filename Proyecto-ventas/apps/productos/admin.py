from django.contrib import admin
from .models import Producto
 
 
@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
 
    list_display = (
        'nombre_producto',
        'codigo',
        'precio_unitario',
        'porcentaje_iva',
        'estado'
    )
 
    search_fields = (
        'nombre_producto',
        'codigo'
    )
 
    list_filter = (
        'estado',
    )
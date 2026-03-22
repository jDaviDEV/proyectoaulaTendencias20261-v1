from django.contrib import admin
from .models import Cotizacion, ItemCotizacion
 
 
class ItemCotizacionInline(admin.TabularInline):
    model = ItemCotizacion
    extra = 1
    fields = ['producto', 'cantidad']
 
 
@admin.register(Cotizacion)
class CotizacionAdmin(admin.ModelAdmin):
 
    list_display = (
        'id',
        'cliente',
        'fecha_emision',
        'estado',
        'total'
    )
 
    list_filter = (
        'estado',
        'fecha_emision'
    )
 
    search_fields = (
        'cliente__nombre',
    )
 
    inlines = [
        ItemCotizacionInline
    ]
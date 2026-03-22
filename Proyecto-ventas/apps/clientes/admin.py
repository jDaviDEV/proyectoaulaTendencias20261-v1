from django.contrib import admin
from .models import Cliente
 
 
@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
 
    list_display = (
        'nombre',
        'identificacion',
        'regimen_tributario',
        'email',
        'telefono'
    )
 
    search_fields = (
        'nombre',
        'identificacion',
        'email'
    )
 
    list_filter = (
        'regimen_tributario',
    )
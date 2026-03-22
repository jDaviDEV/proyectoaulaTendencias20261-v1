from django.db import models
from apps.clientes.models import Cliente
from apps.productos.models import Producto
 
class Cotizacion(models.Model):
    class Estado(models.TextChoices):
        BORRADOR = 'borrador', 'Borrador'
        ENVIADA = 'enviada', 'Enviada'
        ACEPTADA = 'aceptada', 'Aceptada'
        RECHAZADA = 'rechazada', 'Rechazada'
        VENCIDA = 'vencida', 'Vencida'
 
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, related_name='Cotizaciones')
    fecha_emision = models.DateField("Fecha de Emisión",auto_now_add=True)
    fecha_vencimiento = models.DateField("Fecha de Vencimiento")
    subtotal = models.DecimalField("Subtotal", max_digits=20, decimal_places=2, default=0)
    iva = models.DecimalField("Iva", max_digits=20, decimal_places=2, default=0)
    total = models.DecimalField("Total", max_digits=20, decimal_places=2, default=0)
    estado=models.CharField(max_length=20, choices=Estado.choices,default=Estado.BORRADOR)
 
    def __str__(self):
        return f"Cotización {self.id} - {self.cliente}"
 
class ItemCotizacion(models.Model):
    cotizacion = models.ForeignKey(Cotizacion, on_delete=models.CASCADE,related_name='items')
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.IntegerField("Cantidad")
    precio = models.DecimalField("Precio", max_digits=10, decimal_places=2)
    subtotal = models.DecimalField("Subtotal", max_digits=10, decimal_places=2)
 
    def save(self, *args, **kwargs):
 
   
        self.precio = self.producto.precio_unitario
        self.subtotal = self.precio * self.cantidad
        super().save(*args, **kwargs)
        items = self.cotizacion.items.all()
        subtotal = sum(item.subtotal for item in items)
        iva_total = sum(
            item.subtotal * (item.producto.porcentaje_iva / 100)
            for item in items
        )
 
        total = subtotal + iva_total
 
        self.cotizacion.subtotal = subtotal
        self.cotizacion.iva = iva_total
        self.cotizacion.total = total
 
        self.cotizacion.save()
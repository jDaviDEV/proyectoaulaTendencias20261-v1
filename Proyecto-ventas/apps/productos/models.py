from django.db import models
 
 
class Producto(models.Model):
 
    class Estado(models.TextChoices):
        ACTIVO = 'activo', 'Activo'
        INACTIVO = 'inactivo', 'Inactivo'
 
    nombre_producto = models.CharField("Nombre del Productos", max_length=200)
    codigo = models.CharField("Código del Producto", max_length=50, unique = True)
    descripcion = models.TextField("Descripción del producto")
    unidad_medida = models.CharField("Unidad de Medida", max_length=50)
    precio_unitario = models.DecimalField("Precio Unidad", max_digits=10,decimal_places=2)
    porcentaje_iva = models.DecimalField("Iva",max_digits=5, decimal_places=2, default = 19)
    estado = models.CharField("Estado del Producto", max_length=20, choices=Estado.choices, default=Estado.ACTIVO)
 
    def __str__(self):
        return self.nombre_producto
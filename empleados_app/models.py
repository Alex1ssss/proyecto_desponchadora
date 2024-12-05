from django.db import models

# Create your models here.

class Empleados(models.Model):
    id_empleado = models.PositiveIntegerField(primary_key=True)
    nombre_empleado= models.CharField(max_length=20)
    telefono_empleado=models.PositiveBigIntegerField()
    correo_electronico=models.EmailField(max_length=20)
    direccion=models.CharField(max_length=20)
    puesto_empleado= models.CharField(max_length=10)
    fecha_contratacion=models.DateField()


    def __str__(self):
        return self.id_empleado
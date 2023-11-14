from django.db import models

class Proveedor(models.Model):
    nombre = models.CharField(max_length=100)
    telefono = models.CharField(max_length=8)
    persona_a_cargo = models.CharField(max_length=100)
     
    def __str__(self):
        return f"Proveedor: {self.nombre}, Telefono: {self.telefono}"


class Fruta(models.Model):
    nombre = models.CharField(max_length=100)
    cantidad = models.PositiveIntegerField()
    proveedor = models.ForeignKey(Proveedor, on_delete=models.CASCADE)

    def __str__(self):
        return f"Fruta: {self.nombre}"
    


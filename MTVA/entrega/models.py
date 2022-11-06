from django.db import models

# Create your models here.
class Familiar(models.Model):

    nombre = models.CharField(max_length = 40)
    apellido = models.CharField(max_length = 40)
    edad = models.IntegerField()
    parentesco = models.CharField(max_length = 40)
    nacimiento = models.DateField()
    profesion = models.CharField( max_length=30)

    def __str__(self):
        return f"Nombre: {self.nombre} - Apellido: {self.apellido} - Edad: {self.edad} - Parentesco: {self.parentesco}"
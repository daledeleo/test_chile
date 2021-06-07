from django.db import models
from django import forms

from django.core.validators import RegexValidator, MinValueValidator

# Validaciones
alfanumeric = RegexValidator(r'^[a-zA-Z\d\-_\s]+$', 'Solo carácteres alfanuméricos son permitidos.')
min_max = RegexValidator(r'^[0-9A-Za-z]{6,}$', 'Dede ingresar al menos 6 caracteres.')
#Manzana, coliflor, bombilla, derecha, izquierda, rojo, azul)
#ofuscaciones = RegexValidator(r'^(?!Manzana|coliflor|bombilla|derecha|izquierda|rojo|azul)([a-zA-Z0-9]+)$' ,message="Por favor no use ninguna de estas palabras:Manzana, coliflor, bombilla, derecha, izquierda, rojo, azul ")
# validators

# Create your models here.
class Estrella(models.Model):
    id=models.AutoField(primary_key = True)
    nombres = models.CharField(max_length = 40 , default = "")
    apellidos = models.CharField(max_length = 40 , default = "")

    def __str__ (self):
        return self.nombres + " " + self.apellidos

class Comentario(models.Model):
    id=models.AutoField(primary_key = True)
    nickname = models.CharField(max_length=8, validators = [alfanumeric, min_max])
    comentario = models.CharField(max_length = 120)
    valoracion = models.IntegerField(choices= [(-2,"Negativo"),(1,"Positivo")])
    color = models.CharField(max_length=4, choices = [("red","rojo"),("blue","Azul")], default="rojo")
    id_estrella = models.ForeignKey(Estrella, on_delete= models.DO_NOTHING)

    def __str__ (self):
        return str(self.id)

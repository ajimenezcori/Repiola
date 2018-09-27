from django.db import models


# Create your models here.

class Product(models.Model):
    producto_nombre = models.CharField(max_length = 180)
    producto_precio = models.IntegerField()

    def __str__(self):
        return (self.producto_nombre+' : '+str(self.producto_precio))

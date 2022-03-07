from django.db import models
from acceso.models import Usuario

class Libro(models.Model):
 
    titulo = models.CharField(max_length=100)
    descripcion = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    usuarios = models.ForeignKey(Usuario, related_name="libros", on_delete=models.CASCADE)
    # favorito = models.ManyToManyField(Usuario, related_name="favoritos")


    def __str__(self):
        return self.titulo


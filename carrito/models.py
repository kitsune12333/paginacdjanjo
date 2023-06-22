from django.conf import settings
from django.db import models
from django.db.models import Model


class Publicacion(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    price = models.IntegerField()
    upload = models.ImageField(upload_to="productos", null=True)
    descripcion = models.TextField()

    def __str__(self):
        return self.title
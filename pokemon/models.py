from django.db import models
from tipo.models import Tipo


class Pokemon(models.Model):
    nome = models.CharField(max_length=50)
    elemento = models.ManyToManyField(Tipo)
    sprite = models.ImageField(upload_to='sprites', null=True, blank=True)

    def __str__(self):
        return self.nome

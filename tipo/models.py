from django.db import models


class Elementos(models.Model):
    elemento = models.CharField(max_length=20)

    def __str__(self):
        return self.elemento

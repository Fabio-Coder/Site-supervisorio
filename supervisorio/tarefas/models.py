from django.db import models

# Create your models here.

class Tarefa(models.Model):
    nome = models.CharField(max_length=140)
    feito = models.BooleanField(default=False)
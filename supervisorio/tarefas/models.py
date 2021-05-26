from django.db import models

# Create your models here.

class Tarefa(models.Model):
    name = models.CharField(max_length=140)
    done = models.BooleanField(default=False)
    objects = models.Manager()
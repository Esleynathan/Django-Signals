from django.db import models

class Pessoa(models.Model):
    nome = models.CharField(max_length=100)

x = Pessoa(nome = 'esley')
x.save()
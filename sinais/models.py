from django.db import models
from django.db.models.signals import post_save

class Pessoa(models.Model):
    nome = models.CharField(max_length=50)
    email = models.EmailField()
    telefone = models.CharField(max_length=20)

    def __str__(self) -> str:
        return self.nome
    
def envia_sinal(sender, instance, created, **kwargs):
    print('Fui chamada')

post_save.connect(envia_sinal, sender=Pessoa)
from django.db import models
from django.db.models.signals import post_save

class Pessoa(models.Model):
    nome = models.CharField(max_length=50)
    email = models.EmailField()
    telefone = models.CharField(max_length=20)

    def __str__(self) -> str:
        return self.nome
    
def envia_sinal(sender, instance, created, **kwargs):
    if created:
        print('Estou sendo criada.')
    else:
        print('Estou sendo alterada.')
        print(instance.nome)
        print(instance.email)        
        print(instance.telefone)

post_save.connect(envia_sinal, sender=Pessoa)
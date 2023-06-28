from django.db import models
from django.db.models.signals import post_save

class Pessoa(models.Model):
    nome = models.CharField(max_length=50)
    email = models.EmailField()
    telefone = models.CharField(max_length=20)

    def __str__(self) -> str:
        return self.nome

class Historico(models.Model):
    nome = models.CharField(max_length=50)
    email = models.EmailField()
    telefone = models.CharField(max_length=20)
    pessoa = models.ForeignKey(Pessoa, on_delete=models.DO_NOTHING)
    
def envia_sinal(sender, instance, created, **kwargs):
    x = Historico(nome=instance.nome,
                email=instance.email,
                telefone=instance.telefone,
                pessoa=instance
                )
    x.save()
    print('Histórico cadastrado')

post_save.connect(envia_sinal, sender=Pessoa)
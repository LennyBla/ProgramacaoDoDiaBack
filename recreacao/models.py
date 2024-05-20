from django.db import models
from django.contrib.auth.models import User as AuthUser 
from django.utils import timezone

import uuid

class User(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    username = models.CharField(max_length=100, blank=True, null=True)
    email = models.EmailField(max_length=254, unique=True)  
    password = models.CharField(max_length=100)
        
    def __str__(self):
        return self.email
     
class Recreacao(models.Model):
    nome = models.CharField(max_length=50)

    def __str__(self):
        return self.nome

class Kid(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    nome = models.CharField(max_length=100)
    idade = models.IntegerField()
    responsaveis = models.CharField(max_length=100)
    obs = models.CharField(max_length=500, blank=True, null=True)
    email = models.EmailField(max_length=254, blank=True, null=True)
    numeroContato = models.CharField(max_length=20, blank=True, null=True)
    numeroApartamento = models.CharField(max_length=10)
    horarioCheckout = models.DateTimeField()

    class Meta:
        unique_together = (('nome', 'numeroApartamento'),)
        ordering = ['nome']

    def save(self, *args, **kwargs):
        self.horarioCheckout = self.horarioCheckout.isoformat()
        super().save(*args, **kwargs)

    def deletar_se_hospedagem_expirada(self):
        hora_atual = timezone.now()
        diferenca = hora_atual - self.horarioCheckout
        if diferenca.total_seconds() > 3600:
            self.delete()

class Card(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    titulo = models.CharField(max_length=100)
    descricao = models.TextField()
    
    
    def __str__(self):
        return self.titulo

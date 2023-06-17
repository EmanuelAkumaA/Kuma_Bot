from django.db import models

# Create your models here.

# Criar Grupo em redes 
class Grupo(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.CharField(max_length=100)
    
    def __self__ (self):
        return self.nome

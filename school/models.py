from django.db import models

# Create your models here.
# Model de Níveis
class Nivel(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    ordem = models.IntegerField()
    
    def __str__(self):
        return self.nome
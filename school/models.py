from django.db import models
from django.contrib.auth.models import User

# Create your models here.
# Model de Níveis
class Nivel(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    ordem = models.IntegerField()
    
    def __str__(self):
        return self.nome

# Model dos Professores    
class Professor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    telefone = models.CharField(max_length=20)
    materia = models.CharField(max_length=100)
    ativo = models.BooleanField(default=True)
    criado_em = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.user.username
    
# Model dos Monitores
class Monitor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    professor_responsavel = models.ForeignKey(Professor, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.user.username
    
# Model dos Alunos
class Aluno(models.Model):
    nome = models.CharField(max_length=100)
    telefone = models.CharField(max_length=50)
    
    def __str__(self):
        return self.nome
    
# Model de Turmas
class Turmas(models.Model):
    nome = models.CharField(max_length=100)
    nivel = models.ForeignKey(Nivel, on_delete=models.CASCADE)
    professor = models.ForeignKey(Professor, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.nome
    
# Model de Progressão do Aluno
class ProgressoAluno(models.Model):
    aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE)
    nivel = models.ForeignKey(Nivel, on_delete=models.CASCADE)
    
    data_inicio = models.DateField()
    data_conclusao = models.DateField(null=True, blank=True)
    
    aprovado = models.BooleanField(default=False)
    
    def __str__(self):
        return f"{self.aluno} - {self.nivel}"
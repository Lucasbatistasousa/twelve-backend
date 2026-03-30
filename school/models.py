from django.db import models
from django.conf import settings

# Create your models here.

# Model das Igrejas
class Igreja(models.Model):
    nome = models.CharField(max_length=200)
    cidade = models.CharField(max_length=100)
    estado = models.CharField(max_length=2)
    cnpj = models.CharField(max_length=18, blank=True, null=True)
    
    ativa = models.BooleanField(default=True)
    criado_em = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.nome} - {self.cidade}/{self.estado}"
    
    class Meta:
        verbose_name = 'Igreja'
        verbose_name_plural = 'Igrejas'
        ordering = ['nome']

# Model de Níveis
class Nivel(models.Model):
    igreja = models.ForeignKey(Igreja, on_delete=models.CASCADE, null=True)
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    ordem = models.IntegerField()
    
    def __str__(self):
        return self.nome
    
    class Meta: 
        ordering = ["ordem"]
        verbose_name = "Nível"
        verbose_name_plural = "Níveis"

# Model dos Professores    
class Professor(models.Model):
    igreja = models.ForeignKey(Igreja, on_delete=models.CASCADE, null=True)
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    telefone = models.CharField(max_length=20)
    materia = models.CharField(max_length=100)
    ativo = models.BooleanField(default=True)
    criado_em = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name = "Professor"
        verbose_name_plural = "Professores"
    
# Model dos Monitores
class Monitor(models.Model):
    igreja = models.ForeignKey(Igreja, on_delete=models.CASCADE, null=True)
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    professor_responsavel = models.ForeignKey(Professor, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name = "Monitor"
        verbose_name_plural = "Monitores"
    
# Model dos Alunos
class Aluno(models.Model):
    igreja = models.ForeignKey(Igreja, on_delete=models.CASCADE, null=True)
    nome = models.CharField(max_length=100)
    telefone = models.CharField(max_length=50)
    
    def __str__(self):
        return self.nome
    
    class Meta:
        verbose_name = "Aluno"
        verbose_name_plural = "Alunos"
        ordering = ['nome']
    
# Model de Turmas
class Turma(models.Model):
    igreja = models.ForeignKey(Igreja, on_delete=models.CASCADE, null=True)
    nome = models.CharField(max_length=100)
    nivel = models.ForeignKey(Nivel, on_delete=models.CASCADE)
    professor = models.ForeignKey(Professor, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.nome
    
    class Meta:
        verbose_name = 'Turma'
        verbose_name_plural = 'Turmas'
    
# Model de Progressão do Aluno
class ProgressoAluno(models.Model):
    aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE)
    nivel = models.ForeignKey(Nivel, on_delete=models.CASCADE)
    turma = models.ForeignKey(Turma, on_delete=models.CASCADE)
    
    data_inicio = models.DateField()
    data_conclusao = models.DateField(null=True, blank=True)
    
    aprovado = models.BooleanField(default=False)
    
    def __str__(self):
        return f"{self.aluno} - {self.nivel}"
    
    class Meta:
        verbose_name = 'Progresso do Aluno'
        verbose_name_plural = 'Progressos dos Alunos'
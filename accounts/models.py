from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
# Custom User
class CustomUser (AbstractUser):
    class Role(models.TextChoices):
        ADMIN = 'admin', 'Admin'
        COORDENADOR = 'coordenador', 'Coordenador'
        SECRETARIA = 'secretaria', 'Secretaria'
        PROFESSOR = ' professor', 'Professor'
        MONITOR = 'monitor', "Monitor"
        ALUNO = 'aluno', 'Aluno'
    
    role = models.CharField(
        max_length = 20,
        choices = Role.choices,
        default = Role.ALUNO
    )
    # Liga o usuário à sua igreja
    # null=True → superusuário admin do sistema não precisa de igreja
    # blank=True → permite salvar o formulário sem igreja (para o admin do sistema)
    # related_name → permite acessar os usuários de uma igreja com igreja.usuarios.all()
    igreja = models.ForeignKey(
        'school.Igreja',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='usuarios'
    )
    
    def __str__(self):
        return f"{self.username} - {self.role}"
    
    # Propriedades auxiliares — facilitam verificar o role em qualquer lugar do código
    # Ex: if request.user.is_professor → muito mais legível que if request.user.role == 'professor'
    @property
    def is_admin(self):
        return self.role == self.Role.ADMIN

    @property
    def is_coordenador(self):
        return self.role == self.Role.COORDENADOR

    @property
    def is_secretaria(self):
        return self.role == self.Role.SECRETARIA

    @property
    def is_professor(self):
        return self.role == self.Role.PROFESSOR

    @property
    def is_monitor(self):
        return self.role == self.Role.MONITOR

    @property
    def is_aluno(self):
        return self.role == self.Role.ALUNO
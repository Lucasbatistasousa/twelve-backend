from django.contrib import admin
from .models import Nivel, Professor, Monitor, Turmas, Aluno, ProgressoAluno

# Register your models here.
admin.site.register(Nivel)
admin.site.register(Professor)
admin.site.register(Monitor)
admin.site.register(Turmas)
admin.site.register(Aluno)
admin.site.register(ProgressoAluno)
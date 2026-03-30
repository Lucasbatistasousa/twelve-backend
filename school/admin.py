from django.contrib import admin
from .models import Igreja, Nivel, Professor, Monitor, Turma, Aluno, ProgressoAluno

# Register your models here.
admin.site.register(Igreja)
admin.site.register(Nivel)
admin.site.register(Professor)
admin.site.register(Monitor)
admin.site.register(Turma)
admin.site.register(Aluno)
admin.site.register(ProgressoAluno)
# Permissões dos usuários

from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied

# LoginRequiredMixin já garante que o usuário está logado
# Herdamos dele e adicionamos a verificação de role

class AdminRequiredMixin(LoginRequiredMixin):
    # Só admin passa
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_admin:
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)
    
class CoordenadorOuAcimaRequiredMixin(LoginRequiredMixin): 
    # Cordenador, Admin passam
    def dispatch(self, request, *args, **kwargs):
        if not (request.user.is_admin or request.user.is_coordenador):
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)  
    
class SecretariaOuAcimaRequiredMixin(LoginRequiredMixin):
    # Secretária, Coordenador e Admin passam
    def dispatch(self, request, *args, **kwargs):
        allowed = (
            request.user.is_admin or
            request.user.is_coordenador or
            request.user.is_secretaria
        )
        if not allowed:
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)
    
class ProfessorOuAcimaRequiredMixin(LoginRequiredMixin):
    # Professor, Monitor, Secretária, Coordenador, Admin passam
    def dispatch(self, request, *args, **kwargs):
        allowed = (
            request.user.is_admin or
            request.user.is_coordenador or
            request.user.is_secretaria or
            request.user.is_professor or
            request.user.is_monitor
        )
        if not allowed:
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)
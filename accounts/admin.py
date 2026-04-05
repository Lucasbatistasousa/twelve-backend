from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    # Campos exibidos na listagem de usuários
    list_display = ('username', 'email', 'first_name', 'last_name', 'role', 'igreja', 'is_staff')
    
    # Filtros na barra lateral direita
    list_filter = ('role', 'igreja', 'is_staff', 'is_active')
    
    # Adiciona os campos 'role' e 'igreja' na página de edição do usuário
    # fieldsets define as seções da página — estamos adicionando uma seção nova
    fieldsets = UserAdmin.fieldsets + (
        ('Perfil XII', {
            'fields': ('role', 'igreja')
        }),
    )
    
    # Campos exibidos ao criar um usuário novo pelo admin
    add_fieldsets = UserAdmin.add_fieldsets + (
        ('Perfil XII', {
            'fields': ('role', 'igreja')
        }),
    )

admin.site.register(CustomUser, CustomUserAdmin)
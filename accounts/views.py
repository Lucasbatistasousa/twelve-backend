from django.shortcuts import render

from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

# Create your views here.

def login_view(request):
    # Se o usuário estiver logado, manda direto para o dashboard
    if request.user.is_authenticated:
        return redirect('dashboard')
    
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        # O authenticated verifica se o usuário e senha estão corretos
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            # Redireciona para onde o usuário tentou acessar antes do login
            # ou para o dashboard se não havia destino
            next_url = request.GET.get('next', 'dashboard')
            return redirect(next_url)
        else:
            return render(request, 'accounts/login.html', {
                'error': 'Usuário ou senha incorretos'
            })
    return render(request, 'accounts/login.html')

@login_required
def logout_view(request):
    logout(request)
    return redirect('login')

@login_required
def dashboard_view(request):
    # Redireciona o usuário para o dashboard correto baseado na role
    user = request.user
    
    if user.is_admin or user.is_coordenador or user.is_secretaria:
        return render(request, 'accounts/dashboard_admin.html')
    elif user.is_professor or user.is_monitor:
        return render(request, 'accounts/dashboard_professor.html')
    elif user.is_aluno:
        return render (request, 'accounts/dashboard_aluno.html')
    
    return render(request, 'accounts/dasboard.html')
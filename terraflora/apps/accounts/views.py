from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.shortcuts import render, redirect
from django.core.exceptions import ValidationError
from .models import CustomUser

def home(request):
    """View para renderizar a página inicial."""
    return render(request, 'accounts/home.html')  # Corrigido para refletir a estrutura atual

def menu(request):
    """View para renderizar a página do menu."""
    return render(request, 'accounts/menu.html')  # Corrigido para refletir a estrutura atual

def logoff(request):
    """View para realizar o logoff do usuário."""
    logout(request)
    messages.success(request, 'Você foi desconectado com sucesso.')
    return redirect('home')  # Redireciona para a URL nomeada 'home'

def register(request):
    """View para registrar um novo usuário."""
    if request.method == 'POST':
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')
        full_name = request.POST.get('full_Name')
        cpf = request.POST.get('cpf')
        phone_number = request.POST.get('phone_number')
        street = request.POST.get('street')
        home_number = request.POST.get('home_number')
        city = request.POST.get('city')
        state = request.POST.get('state')
        country = request.POST.get('country')

        # Validação básica
        if not email or not username or not password:
            messages.error(request, 'Por favor, preencha todos os campos obrigatórios.')
            return render(request, 'accounts/register.html')  # Corrigido para refletir a estrutura atual

        # Criação do usuário
        try:
            user = CustomUser(
                email=email,
                username=username,
                full_Name=full_name,
                cpf=cpf,
                phone_number=phone_number,
                street=street,
                home_number=home_number,
                city=city,
                state=state,
                country=country,
            )
            user.set_password(password)  # Criptografa a senha
            user.full_clean()  # Valida os campos do modelo
            user.save()

            login(request, user)  # Faz login automaticamente após o registro
            messages.success(request, 'Registro realizado com sucesso!')
            return redirect('menu')  # Redireciona para a página do menu

        except ValidationError as e:
            messages.error(request, f"Erro: {e}")
            return render(request, 'accounts/register.html')  # Corrigido para refletir a estrutura atual

    return render(request, 'accounts/register.html')  # Corrigido para refletir a estrutura atual

def user_login(request):
    """View para realizar o login do usuário."""
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        # Autenticação do usuário
        user = authenticate(request, username=email, password=password)
        
        if user is not None:
            login(request, user)
            messages.success(request, 'Login realizado com sucesso!')
            return redirect('menu')  # Redireciona para a página do menu
        else:
            messages.error(request, 'E-mail ou senha inválidos.')
            return render(request, 'accounts/login.html')  # Corrigido para refletir a estrutura atual

    return render(request, 'accounts/login.html')  # Corrigido para refletir a estrutura atual

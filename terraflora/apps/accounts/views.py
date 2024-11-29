from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.shortcuts import render, redirect
from django.core.exceptions import ValidationError
from django.contrib.auth.decorators import login_required
from .models import CustomUser
from apps.crops.utils import add_example_crops
from apps.farm.models import Farm

@login_required
def home(request):
    farms = Farm.objects.filter(user=request.user)
    return render(request, 'accounts/home.html', {'farms': farms})

def menu(request):
    return render(request, 'menu.html')

def logoff(request):
    logout(request)
    messages.success(request, 'Você saiu com sucesso.')
    return redirect('login')

def register(request):
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
            messages.error(request, 'Preencha todos os campos obrigatórios.')
            return render(request, 'accounts/register.html')

        # Criar o usuário
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
            user.set_password(password)  # Define a senha criptografada
            user.full_clean()  # Valida os campos do modelo
            user.save()
            
            add_example_crops(user)
            
            login(request, user)  # Faz o login automático após o registro
            messages.success(request, 'Registro bem-sucedido!')
            return redirect('home')

        except ValidationError as e:
            messages.error(request, f"Erro: {e}")
            return render(request, 'accounts/register.html')

    return render(request, 'accounts/register.html')

def user_login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        # Autenticar o usuário
        user = authenticate(request, username=email, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, 'Login realizado com sucesso!')
            return redirect('home')  # Redireciona para a página home após login
        else:
            messages.error(request, 'Email ou senha inválidos.')
            return render(request, 'accounts/login.html')

    return render(request, 'accounts/login.html')

def imersao(request):
    return render(request, 'accounts/imersao.html') # Inclua o caminho correto para o template

@login_required
def edit_user(request):
    user = request.user  # Get the logged-in user

    if request.method == 'POST':
        # Collect data from the form
        email = request.POST.get('email')
        full_name = request.POST.get('full_name')
        phone_number = request.POST.get('phone_number')
        street = request.POST.get('street')
        home_number = request.POST.get('home_number')
        city = request.POST.get('city')
        state = request.POST.get('state')
        country = request.POST.get('country')
        current_password = request.POST.get('current_password')

        # Check if the current password is correct
        if not user.check_password(current_password):
            messages.error(request, 'Senha atual incorreta.')
            return render(request, 'accounts/edit_user.html', {'user': user})

        # Update user details
        user.email = email
        user.full_name = full_name
        user.phone_number = phone_number
        user.street = street
        user.home_number = home_number
        user.city = city
        user.state = state
        user.country = country

        try:
            user.full_clean()  # Validate the updated fields
            user.save()  # Save the updated user
            messages.success(request, 'Dados atualizados com sucesso!')
            return redirect('home')

        except ValidationError as e:
            messages.error(request, f"Erro ao atualizar: {e}")
            return render(request, 'accounts/edit_user.html', {'user': user})

    return render(request, 'accounts/edit_user.html', {'user': user})

@login_required
def delete_account(request):
    user = request.user  # Get the logged-in user

    if request.method == 'POST':
        current_password = request.POST.get('current_password')

        # Check if the current password is correct
        if not user.check_password(current_password):
            messages.error(request, 'Senha atual incorreta.')
            return render(request, 'accounts/delete_account.html')

        # Delete the user
        user.delete()
        messages.success(request, 'Conta deletada com sucesso. Sentiremos sua falta!')
        return redirect('login')  # Redirect to login page after deletion

    return render(request, 'accounts/delete_account.html')

@login_required
def user_account(request):
    return render(request, 'accounts/user_account.html')
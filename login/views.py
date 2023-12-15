from django.contrib.auth import login
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import CustomLoginForm

def login_view(request):
    if request.method == 'POST':
        form = CustomLoginForm(request.POST)
        if form.is_valid():
            # Autenticação do usuário
            user = form.get_user()
            login(request, user)
            messages.success(request, 'Login bem-sucedido.')
            return redirect('home')  # Substitua 'home' pelo nome da sua URL home
        else:
            messages.error(request, 'Credenciais inválidas. Por favor, tente novamente.')
    else:
        form = CustomLoginForm()

    return render(request, 'login.html', {'form': form})

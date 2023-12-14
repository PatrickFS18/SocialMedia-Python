from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import RegisterForm

def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            # Salve o usuário no banco de dados
            form.save()
            # Adicione uma mensagem de sucesso
            messages.success(request, 'Registro bem-sucedido. Faça login para continuar.')
            # Redirecione para a página de login ou outra página desejada
            return redirect('login:login')
        else:
            # Adicione uma mensagem de erro
            messages.error(request, 'Corrija os erros no formulário.')
    else:
        form = RegisterForm()

    return render(request, 'register.html', {'form': form})

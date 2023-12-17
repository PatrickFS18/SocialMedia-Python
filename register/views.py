from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import RegisterForm

def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        messages.error(request,'Entrou aqui no 1')
        if form.is_valid():
            messages.error(request,'Entrou aqui no 2')
            
            # Salve o usuário no banco de dados
            form.save()
            # Adicione uma mensagem de sucesso
            messages.success(request, 'Registro bem-sucedido. Faça login para continuar.')
            # Redirecione para a página de login ou outra página desejada
            return redirect('login:login')
        else:
            messages.error(request,'Entrou aqui no 3')

            messages.error(request, 'Corrija os erros no formulário.')
    else:
        form = RegisterForm()
        messages.error(request,'Entrou aqui no 4')
        
    messages.error(request,'Entrou aqui no 5')
    return render(request, 'register.html', {'form': form})

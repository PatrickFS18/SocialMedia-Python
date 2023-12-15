from django.contrib import messages
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from .forms import CustomLoginForm

class CustomLoginView(LoginView):
    template_name = 'login.html'
    authentication_form = CustomLoginForm

    def form_valid(self, form):
        # Você pode adicionar lógica aqui se necessário
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, 'Credenciais inválidas. Por favor, tente novamente.')
        return super().form_invalid(form)

def home_view(request):
    return render(request, 'home.html')

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
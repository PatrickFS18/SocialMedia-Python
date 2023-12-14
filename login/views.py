from django.contrib.auth.views import LoginView
from django.shortcuts import render

def home_view(request):
    return render(request, 'home.html')

class CustomLoginView(LoginView):
    template_name = 'login.html'
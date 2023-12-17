from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import CustomLoginForm  
def login_view(request):
    if request.method == 'POST':
        form = CustomLoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            senha = form.cleaned_data['senha']

            # Authenticate the user
            user = authenticate(request, email=email, password=senha)

            if user is not None:
                # Log the user in
                login(request, user)
                return redirect('home')  # Replace with your actual success page URL
            else:
                # Authentication failed, handle accordingly
                return redirect('home') 
                return render(request, 'login.html', {'form': form, 'error': 'Invalid credentials'})
    else:
        form = CustomLoginForm()

    return render(request, 'login.html', {'form': form})

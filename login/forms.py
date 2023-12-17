from django import forms
from register.models import Usuario

class CustomLoginForm(forms.ModelForm):
    senha = forms.CharField(widget=forms.PasswordInput)
    email = forms.EmailField()
    class Meta:
        model = Usuario
        fields = ['email', 'senha']
from django import forms

class RegisterForm(forms.Form):
    senha = forms.CharField(widget=forms.PasswordInput)
    email = forms.EmailField()

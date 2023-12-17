from django import forms

class CustomLoginForm(forms.Form):
    senha = forms.CharField(widget=forms.PasswordInput)
    email = forms.EmailField()

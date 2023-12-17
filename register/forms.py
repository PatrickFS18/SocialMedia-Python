from django import forms

class RegisterForm(forms.ModelForm):
    senha = forms.CharField(widget=forms.PasswordInput)
    email = forms.EmailField()
   
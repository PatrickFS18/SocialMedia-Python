from django import forms

class CustomLoginForm(forms.ModelForm):
    senha = forms.CharField(widget=forms.PasswordInput)
    email = forms.EmailField()
   
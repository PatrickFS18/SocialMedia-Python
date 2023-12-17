from django import forms

class RegisterForm(forms.ModelForm):
    senha = forms.CharField(widget=forms.PasswordInput)
    email = forms.EmailField()
    def __str__(self):
        return self.name
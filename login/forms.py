from django import forms
from register.models import Usuario

class CustomLoginForm(forms.ModelForm):
    senha = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = Usuario
        fields = ['email', 'senha']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Remova o campo 'nome' do formulário
        self.fields.pop('nome', None)
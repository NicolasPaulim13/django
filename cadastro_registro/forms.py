from django import forms
from .models import CadastroRegistro

class CadastroRegistroForm(forms.ModelForm):
    class Meta:
        model = CadastroRegistro
        fields = ['nome_paciente', 'email_paciente', 'cpf_paciente', 'data_nascimento_paciente', 'sexo_paciente', 'senha_paciente', 'confirma_senha_paciente']
        widgets = {
            'senha_paciente': forms.PasswordInput(),
            'confirma_senha_paciente': forms.PasswordInput(),
        }

    def clean(self):
        cleaned_data = super().clean()
        senha = cleaned_data.get('senha_paciente')
        confirma_senha = cleaned_data.get('confirma_senha_paciente')

        if senha and confirma_senha and senha != confirma_senha:
            raise forms.ValidationError("As senhas não coincidem.")
        return cleaned_data

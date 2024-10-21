from django import forms
from .models import Consulta

class ConsultaForm(forms.ModelForm):
    class Meta:
        model = Consulta
        fields = ['nome', 'email', 'telefone', 'assunto', 'data', 'horario', 'observacoes']

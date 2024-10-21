from django.db import models
from django.contrib.auth.models import User
from django.conf import settings  # Importando settings para referenciar o modelo User

class CadastroRegistro(models.Model):
    nome_paciente = models.CharField(max_length=100)
    email_paciente = models.EmailField()
    cpf_paciente = models.CharField(max_length=11)
    data_nascimento_paciente = models.DateField()
    sexo_paciente = models.CharField(max_length=1, choices=[('M', 'Masculino'), ('F', 'Feminino'), ('O', 'Outro')])
    senha_paciente = models.CharField(max_length=255)
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True)  # Permitir nulo

    def __str__(self):
        return self.nome_paciente


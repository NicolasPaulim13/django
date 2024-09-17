from django.db import models

class CadastroRegistro(models.Model):
    nome_paciente = models.CharField(max_length=100)
    email_paciente = models.EmailField()
    cpf_paciente = models.CharField(max_length=11)
    data_nascimento_paciente = models.DateField()
    sexo_paciente = models.CharField(max_length=1, choices=[('M', 'Masculino'), ('F', 'Feminino'), ('O', 'Outro')])
    senha_paciente = models.CharField(max_length=100)
    confirma_senha_paciente = models.CharField(max_length=100)

    def __str__(self):
        return self.nome_paciente

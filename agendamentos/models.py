from django.db import models

class Agendamento(models.Model):
    nome_paciente = models.CharField(max_length=100)
    data = models.DateField()
    hora = models.TimeField()
    medico = models.CharField(max_length=100)
    observacoes = models.TextField(blank=True, null=True)

    def __str__(self):
        return f'{self.nome_paciente} - {self.data} {self.hora}'

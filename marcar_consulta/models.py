from django.db import models

class Consulta(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField()
    telefone = models.CharField(max_length=15)
    assunto = models.CharField(max_length=100)
    data = models.DateField()
    horario = models.TimeField()
    observacoes = models.TextField(blank=True, null=True)

    def __str__(self):
        return f'{self.nome} - {self.data} {self.horario}'

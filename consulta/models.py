from django.db import models

class Consulta(models.Model):
    PROCEDIMENTOS_CHOICES = [
        ('avaliacao_diagnostico', 'Avaliação e Diagnóstico'),
        ('tratamentos_restauradores', 'Tratamentos Restauradores'),
        ('tratamentos_periodontais', 'Tratamentos Periodontais'),
        ('odontopediatria', 'Odontopediatria'),
        ('ortodontia', 'Ortodontia'),
        ('odontologia_estetica', 'Odontologia Estética'),
        ('cirurgia_oral', 'Cirurgia Oral'),
        ('proteses_dentarias', 'Próteses Dentárias'),
        ('consultas_emergencia', 'Consultas de Emergência'),
        ('acompanhamento_manutencao', 'Acompanhamento e Manutenção'),
    ]

    nome = models.CharField(max_length=100)
    email = models.EmailField()
    telefone = models.CharField(max_length=15)
    assunto = models.CharField(max_length=50, choices=PROCEDIMENTOS_CHOICES)
    data_hora = models.DateTimeField()
    observacoes = models.TextField()

    def __str__(self):
        return f"{self.nome} - {self.data_hora}"

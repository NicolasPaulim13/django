# Generated by Django 5.1.1 on 2024-10-21 14:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Consulta",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("nome", models.CharField(max_length=100)),
                ("email", models.EmailField(max_length=254)),
                ("telefone", models.CharField(max_length=15)),
                (
                    "assunto",
                    models.CharField(
                        choices=[
                            ("avaliacao_diagnostico", "Avaliação e Diagnóstico"),
                            ("tratamentos_restauradores", "Tratamentos Restauradores"),
                            ("tratamentos_periodontais", "Tratamentos Periodontais"),
                            ("odontopediatria", "Odontopediatria"),
                            ("ortodontia", "Ortodontia"),
                            ("odontologia_estetica", "Odontologia Estética"),
                            ("cirurgia_oral", "Cirurgia Oral"),
                            ("proteses_dentarias", "Próteses Dentárias"),
                            ("consultas_emergencia", "Consultas de Emergência"),
                            (
                                "acompanhamento_manutencao",
                                "Acompanhamento e Manutenção",
                            ),
                        ],
                        max_length=50,
                    ),
                ),
                ("data_hora", models.DateTimeField()),
                ("observacoes", models.TextField()),
            ],
        ),
    ]
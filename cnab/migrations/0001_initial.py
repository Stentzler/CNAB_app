# Generated by Django 4.1.3 on 2022-11-23 18:35

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Transaction",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("tipo", models.CharField(max_length=1)),
                ("data", models.CharField(max_length=15)),
                ("valor", models.CharField(max_length=15)),
                ("cpf", models.CharField(max_length=11)),
                ("cartao", models.CharField(max_length=15)),
                ("hora", models.CharField(max_length=15)),
                ("dono_da_loja", models.CharField(max_length=16)),
                ("nome_da_loja", models.CharField(max_length=21)),
            ],
        ),
    ]
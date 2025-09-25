from django.db import models
from django.contrib.auth.models import User
from datetime import date

class InformacoesFamiliares(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE, related_name='info_familiares')
    conjuge_nome = models.CharField("Nome do Cônjuge", max_length=255, blank=True, null=True)
    conjuge_data_nascimento = models.DateField("Data de Nascimento do Cônjuge", blank=True, null=True)
    endereco = models.CharField("Endereço", max_length=255, blank=True)
    bairro = models.CharField("Bairro", max_length=100, blank=True)
    numero_casa = models.CharField("Número", max_length=20, blank=True)
    complemento = models.CharField("Complemento", max_length=100, blank=True, null=True)
    cidade = models.CharField("Cidade", max_length=100, blank=True)
    cep = models.CharField("CEP", max_length=9, blank=True)

    def __str__(self):
        return f"Informações Familiares de {self.usuario.username}"

class Filho(models.Model):
    info_familiar = models.ForeignKey(InformacoesFamiliares, on_delete=models.CASCADE, related_name='filhos')
    nome = models.CharField("Nome", max_length=255)
    data_nascimento = models.DateField("Data de Nascimento")
    idade = models.PositiveIntegerField("Idade", editable=False, blank=True, null=True)

    def save(self, *args, **kwargs):
        if self.data_nascimento:
            today = date.today()
            self.idade = today.year - self.data_nascimento.year - ((today.month, today.day) < (self.data_nascimento.month, self.data_nascimento.day))
        else:
            self.idade = None
        super().save(*args, **kwargs)

    def __str__(self):
        return self.nome
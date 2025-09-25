from django.db import models
from django.contrib.auth.models import User
from datetime import date

class InformacoesPessoais(models.Model):
    ESTADO_CIVIL_CHOICES = [('solteiro', 'Solteiro(a)'), ('casado', 'Casado(a)'), ('divorciado', 'Divorciado(a)'), ('viuvo', 'Viúvo(a)')]
    ESCOLARIDADE_CHOICES = [('fundamental', 'Ensino Fundamental'), ('medio', 'Ensino Médio'), ('superior', 'Ensino Superior'), ('pos_graduacao', 'Pós-Graduação')]
    
    usuario = models.OneToOneField(User, on_delete=models.CASCADE, related_name='info_pessoais')
    nome_completo = models.CharField("Nome Completo", max_length=255, blank=True)
    foto = models.ImageField("Foto", upload_to='fotos_pessoais/', blank=True, null=True)
    cpf = models.CharField("CPF", max_length=14, unique=True, null=True, blank=True)
    rg = models.CharField("RG", max_length=20, blank=True)
    data_nascimento = models.DateField("Data de Nascimento", null=True, blank=True)
    idade = models.PositiveIntegerField("Idade", editable=False, blank=True, null=True)
    grupo_sanguineo = models.CharField("Grupo Sanguíneo", max_length=5, blank=True)
    telefone = models.CharField("Telefone", max_length=20, blank=True)
    email = models.EmailField("E-mail", unique=True, null=True, blank=True)
    estado_civil = models.CharField("Estado Civil", max_length=20, choices=ESTADO_CIVIL_CHOICES, blank=True)
    escolaridade = models.CharField("Escolaridade", max_length=20, choices=ESCOLARIDADE_CHOICES, blank=True)
    cnh_numero = models.CharField("Nº da CNH", max_length=20, blank=True, null=True)
    cnh_categoria = models.CharField("Categoria da CNH", max_length=5, blank=True, null=True)
    cnh_validade = models.DateField("Validade da CNH", blank=True, null=True)
    titulo_eleitor = models.CharField("Título de Eleitor", max_length=30, blank=True)
    zona = models.CharField("Zona Eleitoral", max_length=10, blank=True)
    secao = models.CharField("Seção Eleitoral", max_length=10, blank=True)
    municipio_votacao = models.CharField("Município de Votação", max_length=100, blank=True)

    def save(self, *args, **kwargs):
        if self.data_nascimento:
            today = date.today()
            self.idade = today.year - self.data_nascimento.year - ((today.month, today.day) < (self.data_nascimento.month, self.data_nascimento.day))
        else:
            self.idade = None
        super().save(*args, **kwargs)

    def __str__(self):
        return self.nome_completo or self.usuario.username
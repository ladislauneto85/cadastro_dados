from django.db import models
from django.contrib.auth.models import User

class InformacoesFuncionais(models.Model):
    POSTO_CHOICES = [
        ('coronel', 'Coronel'), 
        ('tenente_coronel', 'Tenente-Coronel'),  
        ('major', 'Major'), 
        ('capitao', 'Capitão'), 
        ('tenente', 'Tenente'),
        ('aspirante', 'Aspirante'),
        ('subtenente', 'Subtenente'), 
        ('sargento', 'Sargento'), 
        ('cabo', 'Cabo'), 
        ('soldado', 'Soldado')
    ]

    usuario = models.OneToOneField(User, on_delete=models.CASCADE, related_name='info_funcionais')
    nome_guerra = models.CharField("Nome de Guerra", max_length=100, blank=True)
    matricula = models.CharField("Matrícula", max_length=50, unique=True, null=True, blank=True)
    posto_graduacao = models.CharField("Posto/Graduação", max_length=50, choices=POSTO_CHOICES, blank=True)
    data_admissao = models.DateField("Data de Admissão", null=True, blank=True)
    banco = models.CharField("Banco", max_length=100, blank=True)
    agencia = models.CharField("Agência", max_length=20, blank=True)
    conta_corrente = models.CharField("Conta Corrente", max_length=30, blank=True)

    def __str__(self):
        return f'{self.get_posto_graduacao_display()} {self.nome_guerra}' if self.nome_guerra else self.usuario.username


class Documento(models.Model):
    info_funcional = models.ForeignKey(InformacoesFuncionais, on_delete=models.CASCADE, related_name='documentos')
    nome_documento = models.CharField("Nome do Documento", max_length=255)
    arquivo = models.FileField("Arquivo", upload_to='documentos/')

    def __str__(self):
        return self.nome_documento
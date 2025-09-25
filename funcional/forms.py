from django import forms
from .models import InformacoesFuncionais

class InformacoesFuncionaisForm(forms.ModelForm):
    # Adicionar o formato correto no widget
    data_admissao = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date'}, format='%Y-%m-%d'), 
        required=False
    )

    class Meta:
        model = InformacoesFuncionais
        exclude = ['usuario']
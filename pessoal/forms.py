from django import forms
from .models import InformacoesPessoais

class InformacoesPessoaisForm(forms.ModelForm):
    # Adicionar o formato correto no widget
    data_nascimento = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date'}, format='%Y-%m-%d'), 
        required=False
    )
    cnh_validade = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date'}, format='%Y-%m-%d'), 
        required=False
    )

    class Meta:
        model = InformacoesPessoais
        exclude = ['usuario', 'idade']
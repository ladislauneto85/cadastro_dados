from django import forms
from .models import InformacoesFamiliares

class InformacoesFamiliaresForm(forms.ModelForm):
    # Adicionar o formato correto no widget
    conjuge_data_nascimento = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date'}, format='%Y-%m-%d'), 
        required=False
    )
    
    class Meta:
        model = InformacoesFamiliares
        exclude = ['usuario']
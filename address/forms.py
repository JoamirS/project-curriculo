from django import forms
from .models import *


class dadoPessoalForm(forms.ModelForm):
    class Meta:
        model = dadoPessoal
        fields = ['id', 'nome', 'sobrenome', 'nascimento', 'nacionalidade', 'CPF', 'estadocivil', 'naturalidade','uf']


class enderecoUsuarioForm(forms.ModelForm):
    class Meta:
        model = enderecoUsuario
        fields = ['id', 'id_enderecoUsuario', 'rua', 'numero', 'bairro', 'quadra', 'cep']


class formacaoForm(forms.ModelForm):
    class Meta:
        model = formacao
        fields = ['id', 'id_formacao', 'graduacao', 'universidadegraduacao', 'cursograduacao', 'anoformacaograduacao',
        'posgraduacao', 'universidadeposgraduacao', 'cursopos', 'anoformacaoposgraduacao']

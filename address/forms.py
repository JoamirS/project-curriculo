from django import forms
from .models import *


class dadoPessoalForm(forms.ModelForm):
    class Meta:
        model = dadoPessoal
        fields = ['id', 'meu_cpf', 'nome', 'sobrenome', 'nascimento', 'nacionalidade', 'estadocivil', 'naturalidade','uf']


class enderecoUsuarioForm(forms.ModelForm):
    class Meta:
        model = enderecoUsuario
        fields = ['id', 'id_enderecoUsuario', 'rua', 'numero', 'bairro', 'quadra', 'cep']


class formacaoForm(forms.ModelForm):
    class Meta:
        model = formacao
        fields = ['id', 'id_formacao', 'graduacao', 'universidadegraduacao', 'cursograduacao', 'anoformacaograduacao',
        'posgraduacao', 'universidadeposgraduacao', 'cursopos', 'anoformacaoposgraduacao']


class contatoForm(forms.ModelForm):
    class Meta:
        model = contato
        fields = ['id', 'id_formacao', 'email', 'celular1', 'telefone', 'celular2']



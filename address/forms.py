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


class habilidadeForm(forms.ModelForm):
    class Meta:
        model = habilidade
        fields = ['id', 'id_habilidade', 'habilidade1', 'habilidade2', 'habilidade3', 'habilidade4', 'habilidade5',
                  'habilidade6']


class experienciaForm(forms.ModelForm):
    class Meta:
        model = experiencia
        fields = ['id', 'id_experiencia', 'Cargo1', 'TempoCargoEmAnosCargo1', 'Cargo2', 'TempoCargoEmAnosCargo2']

from django.db import models


class dadoPessoal(models.Model):
    id = primary_key = True
    meu_cpf = models.CharField(max_length=11)
    nome = models.CharField(max_length=50)
    sobrenome = models.CharField(max_length=50)
    nascimento = models.DateField()
    nacionalidade = models.CharField(max_length=50)
    estadocivil = models.CharField(max_length=20)
    naturalidade = models.CharField(max_length=30)
    uf = models.CharField(max_length=2)


class enderecoUsuario(models.Model):
    id = primary_key = True
    id_enderecoUsuario = models.ForeignKey(dadoPessoal, on_delete=models.PROTECT)
    rua = models.CharField(max_length=50)
    numero = models.IntegerField()
    bairro = models.CharField(max_length=30)
    quadra = models.IntegerField()
    cep = models.IntegerField()


class formacao(models.Model):
    id = primary_key = True
    id_formacao = models.ForeignKey(dadoPessoal, on_delete=models.PROTECT)
    graduacao = models.CharField(max_length=50)
    universidadegraduacao = models.CharField(max_length=50)
    cursograduacao = models.CharField(max_length=50)
    anoformacaograduacao = models.CharField(max_length=4)
    posgraduacao = models.CharField(max_length=50)
    universidadeposgraduacao = models.CharField(max_length=50)
    cursopos = models.CharField(max_length=50)
    anoformacaoposgraduacao = models.CharField(max_length=4)


class contato(models.Model):
    id = primary_key = True
    id_formacao = models.ForeignKey(dadoPessoal, on_delete=models.PROTECT)
    email = models.EmailField(max_length=255)
    celular1 = models.CharField(max_length=11)
    telefone = models.CharField(max_length=10)
    celular2 = models.CharField(max_length=11)


class habilidade(models.Model):
    id = primary_key = True
    id_habilidade = models.ForeignKey(dadoPessoal, on_delete=models.PROTECT)
    habilidade1 = models.CharField(max_length=50)
    habilidade2 = models.CharField(max_length=50)
    habilidade3 = models.CharField(max_length=50)
    habilidade4 = models.CharField(max_length=50, blank=True, null=True)
    habilidade5 = models.CharField(max_length=50, blank=True, null=True)
    habilidade6 = models.CharField(max_length=50, blank=True, null=True)


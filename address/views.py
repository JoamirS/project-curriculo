from django.shortcuts import render, redirect
from .forms import dadoPessoalForm, enderecoUsuarioForm, formacaoForm, contatoForm
from .models import dadoPessoal, enderecoUsuario, formacao, contato


def homepage(request):
    return render(request, 'address/homepage.html')


def apply(request):
    data = {}
    form = dadoPessoalForm(request.POST or None)

    # validacao
    if form.is_valid():
        form.save()
        return redirect('/')
    data['form'] = form
    return render(request, 'candidato/apply.html', data)


def applyendereco(request):
    dataend = {}
    endereco = enderecoUsuarioForm(request.POST or None)

    #Validacao
    if endereco.is_valid():
        endereco.save()
        return redirect('/')
    dataend['endereco'] = endereco
    return render(request, 'candidato/applyendereco.html', dataend)


def applyformacao(request):
    dataformacao = {}
    formacao = formacaoForm(request.POST or None)

    #validacao
    if formacao.is_valid():
        formacao.save()
        return redirect('/')
    dataformacao['formacao'] = formacao
    return render(request, 'candidato/formacao.html')


def applycontato(request):
    datacontato = {}
    contato = contatoForm(request.POST or None)

    #Validacao
    if contato.is_valid():
        contato.save()
        return redirect('/')
    datacontato['contato'] = contato
    return render(request, 'cadidato/contato')



# def listagem(request):
#     data = {}
#     data['dadoPessoal'] = dadoPessoal.objects.all()
#     return render(request, 'address/list.html', data)
#     print('foi')


def companies(request):
    return render(request, 'empresa/companies.html')


def about(request):
    return render(request, 'sobre/about.html')

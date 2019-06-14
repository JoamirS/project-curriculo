from django.shortcuts import render, redirect
from .forms import dadoPessoalForm, enderecoUsuarioForm, formacaoForm, contatoForm, habilidadeForm
from .models import dadoPessoal, enderecoUsuario, formacao, contato, habilidade


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
    data = {}
    form = enderecoUsuarioForm(request.POST or None)

    #Validacao
    if form.is_valid():
        form.save()
        return redirect('/')
    data['endereco'] = form
    return render(request, 'candidato/applyendereco.html', data)


def applyformacao(request):
    data = {}
    form = formacaoForm(request.POST or None)

    #validacao
    if form.is_valid():
        form.save()
        return redirect('/')
    data['formacao'] = formacao
    return render(request, 'candidato/formacao.html')


def applycontato(request):
    data = {}
    form = contatoForm(request.POST or None)

    #Validacao
    if form.is_valid():
        form.save()
        return redirect('/')
    data['form'] = form
    return render(request, 'candidato/contato.html')


def applyhabilidade(request):
    data = {}
    form = habilidadeForm(request.POST or None)

    #Validacao
    if form.is_valid():
        form.save()
        return redirect('/')
    data['contato'] = form
    return render(request, 'cadidato/habilidade.html')



# def listagem(request):
#     data = {}
#     data['dadoPessoal'] = dadoPessoal.objects.all()
#     return render(request, 'address/list.html', data)
#     print('foi')



def companies(request):
    return render(request, 'empresa/companies.html')


def about(request):
    return render(request, 'sobre/about.html')

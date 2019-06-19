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
        return redirect('/candidato/applyendereco.html')
    data['form'] = form
    return render(request, 'candidato/apply.html', data)


def applyendereco(request):
    data = {}
    formEndereco = enderecoUsuarioForm(request.POST or None)

    #Validacao
    if formEndereco.is_valid():
        formEndereco.save()
        return redirect('/candidato/formacao.html')
    data['formEndereco'] = formEndereco
    return render(request, 'candidato/applyendereco.html', data)


def applyformacao(request):
    data = {}
    formFormacao = formacaoForm(request.POST or None)

    #validacao
    if formFormacao.is_valid():
        formFormacao.save()
        return redirect('/candidato/contato.html')
    data['formFormacao'] = formFormacao
    return render(request, 'candidato/formacao.html', data)


def applycontato(request):
    data = {}
    formContato = contatoForm(request.POST or None)

    #Validacao
    if formContato.is_valid():
        formContato.save()
        return redirect('/cadidato/habilidade.html')
    data['formContato'] = formContato
    return render(request, 'candidato/contato.html', data)


def applyhabilidade(request):
    data = {}
    formHabilidade = habilidadeForm(request.POST or None)

    #Validacao
    if formHabilidade.is_valid():
        formHabilidade.save()
        return redirect('http://127.0.0.1:8000/home')
    data['formHabilidade'] = formHabilidade
    return render(request, 'candidato/habilidade.html', data)



# def listagem(request):
#     data = {}
#     data['dadoPessoal'] = dadoPessoal.objects.all()
#     return render(request, 'address/list.html', data)
#     print('foi')



def companies(request):
    return render(request, 'empresa/companies.html')


def about(request):
    return render(request, 'sobre/about.html')

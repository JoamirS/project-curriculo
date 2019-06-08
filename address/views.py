from django.shortcuts import render
from .forms import *


def homepage(request):
    return render(request, 'address/homepage.html')


def apply(request):
    form = dadoPessoalForm()
    form2 = enderecoUsuarioForm()
    return render(request, 'address/apply.html', {'form': form}, {'form': form2})


def companies(request):
    return render(request, 'address/companies.html')


def about(request):
    return render(request, 'address/about.html')

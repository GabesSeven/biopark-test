from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.paginator import Paginator
from .forms import ApartamentoModelForm, EdificioModelForm, ClienteModelForm
from .models import Apartamento, Cliente, Edificio
from django.db import models


def index(request):
    apartamentos = Apartamento.objects.all()
    apartamento_paginator = Paginator(apartamentos, 4)
    page_num = request.GET.get('page')
    page = apartamento_paginator.get_page(page_num)
    context = {
        'page': page,
    }
    return render(request, 'index.html', context)

def validate_form(request, form):
    if form.is_valid():
        form.save()
        messages.success(request, 'Cadastrado com sucesso.')
        return True
    else:
        messages.error(request, 'Erro ao cadastrar, formulário incorreto.')
        return False


def register(request, pg):
    form_edificio = EdificioModelForm(request.POST, request.FILES)
    form_apartamento = ApartamentoModelForm(request.POST, request.FILES)

    print(f'PG: {pg}')
    if pg != 0 and pg!= 1:
        form_edificio = EdificioModelForm()
        form_apartamento = ApartamentoModelForm()
        context = {
            'form_apartamento': form_apartamento,
            'form_edificio': form_edificio,
        }
        return render(request, 'register.html', context)

    if str(request.user) != 'AnonymousUser':
        if str(request.method) == 'POST' and pg == 0: # formuláro edificio
            validate_form(request, form_edificio)
        elif str(request.method) == 'POST' and pg == 1: # formuláro apartamento
            validate_form(request, form_apartamento)

        form_edificio = EdificioModelForm()
        form_apartamento = ApartamentoModelForm()
    else:
        messages.error(request, 'Usuário não autenticado, entre na guia "Cadastro", digite usuário e senha.')
    context = {
        'form_apartamento': form_apartamento,
        'form_edificio': form_edificio,
    }
    return render(request, 'register.html', context)

def immobile(request, pk, pg):
    apartamento = Apartamento.objects.get(id=pk)
    form_cliente = ClienteModelForm(request.POST, request.FILES)

    if pg == 1:
        apartamento.alugado = True
        if str(request.user) != 'AnonymousUser' and str(request.method) == 'POST' : # formuláro cliente
            if validate_form(request, form_cliente):
                apartamento.save()
        else:
            messages.error(request, 'Usuário não autenticado, entre na guia "Cadastro", digite usuário e senha.')

    form_cliente = ClienteModelForm()
    form_cliente.fields['apartamento'].queryset = Apartamento.objects.filter(id=pk).values_list('id', flat=True)

    if apartamento.alugado:
        cliente = Cliente.objects.get(apartamento=pk)
    else:
        cliente = []

    context = {
        'apartamento': apartamento,
        'cliente': cliente,
        'form_cliente': form_cliente,
    }
    return render(request, 'immobile.html', context)


def sec_bio():
    pass

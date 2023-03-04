from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .forms import ApartamentoModelForm, EdificioModelForm, ClienteModelForm
from .models import Apartamento, Cliente, Edificio

def immobile(request, pk):
    # form_cliente = ClienteModelForm(request.POST, request.FILES)
    print('AQUIIIIIIIII')
    print(f'PG: {pk}')
    # if pg != 0 and pg!= 1 and pg != 2:
        # form_cliente = ClienteModelForm()
    apartamento = get_object_or_404(Apartamento, id=pk)
    context = {
        'apartamento': apartamento,
    }

    return render(request, 'immobile.html', context)

    # return render(request, 'register.html', context)



    # if str(request.user) != 'AnonymousUser':
    # if str(request.method) == 'POST' and pg == 0: # formuláro edificio
        # validate_form(request, form_cliente)
        # form_cliente = ClienteModelForm()
        # context = {
        # 'form_apartamento': form_apartamento,
        # 'form_edificio': form_edificio,
        # 'form_cliente': form_cliente,
        # }

def validate_form(request, form):
    if form.is_valid():
        form.save()
        messages.success(request, 'Cadastrado com sucesso.')
    else:
        messages.error(request, 'Erro ao cadastrar.')

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
        context = {
            'form_apartamento': form_apartamento,
            'form_edificio': form_edificio,
        }
    return render(request, 'register.html', context)

def index(request):
    context = {
        'apartamentos': Apartamento.objects.all()
    }
    return render(request, 'index.html', context)

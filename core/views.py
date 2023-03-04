from django.shortcuts import render
from django.contrib import messages
from django.shortcuts import redirect
from .forms import ApartamentoModelForm, EdificioModelForm, ClienteModelForm
from .models import Apartamento, Cliente, Edificio

def index(request):
    print(f'Request: {request}')

    # if str(request.user) == 'AnonymousUser':
    #     teste = 'Usuário não logado'
    # else:
    #     teste = 'Usuáro logado'
    #     print(f'Email User: {request.user.email}')

    context = {
        'apartamentos': Apartamento.objects.all()
    }
    return render(request, 'index.html', context)

def validate_form(request, form):
    if form.is_valid():
        form.save()
        messages.success(request, 'Cadastrado com sucesso.')
    else:
        messages.error(request, 'Erro ao cadastrar.')

def validate_form(request, form):
    if form.is_valid():
        form.save()
        messages.success(request, 'Cadastrado com sucesso.')
    else:
        messages.error(request, 'Erro ao cadastrar.')

def register(request, pg):

    method = str(request.method)
    form_edificio = EdificioModelForm(request.POST, request.FILES)
    form_apartamento = ApartamentoModelForm(request.POST, request.FILES)

    print(f'PG: {pg}')
    if pg != 0 and pg!= 1 and pg != 2:
        form_edificio = EdificioModelForm()
        form_apartamento = ApartamentoModelForm()
        context = {
            'form_apartamento': form_apartamento,
            'form_edificio': form_edificio,
        }
        return render(request, 'register.html', context)



    if str(request.user) != 'AnonymousUser':
        if method == 'POST' and pg == 0: # formuláro edificio
            validate_form(request, form_edificio)
        elif method == 'POST' and pg == 1: # formuláro apartamento
            validate_form(request, form_apartamento)

    form_edificio = EdificioModelForm()
    form_apartamento = ApartamentoModelForm()
    context = {
        'form_apartamento': form_apartamento,
        'form_edificio': form_edificio,
    }
    return render(request, 'register.html', context)

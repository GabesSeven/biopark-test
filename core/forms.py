from django import forms
from django.db import models
from .models import Cliente, Apartamento, Edificio

class ClienteModelForm(forms.ModelForm):
    # Cliente = forms.ModelChoiceField(queryset=None)

    class Meta(object):
        model = Cliente
        fields = ['nome', 'email', 'cpf', 'apartamento']

    # def __init__(self, *args, **kwargs):
    #     super (ClienteModelForm, self).__init__(*args,**kwargs)
    #     self.fields['apartamento'].queryset = Apartamento.objects.filter(alugado=False)


class EdificioModelForm(forms.ModelForm):
    class Meta(object):
        model = Edificio
        fields = ['nome', 'rua', 'numero', 'complemento', 'cidade',]


class ApartamentoModelForm(forms.ModelForm):
    class Meta(object):
        model = Apartamento
        fields = ['titulo', 'edificio', 'preco', 'descricao', 'imagem', 'numero_quartos', 'numero_banheiros',]

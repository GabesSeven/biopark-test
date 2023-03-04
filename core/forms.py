from django import forms
from .models import Cliente, Apartamento, Edificio

class ClienteModelForm(forms.ModelForm):
    class Meta(object):
        model = Cliente
        fields = ['nome', 'sobrenome', 'email', 'telefone', 'cpf', 'apartamento']

class EdificioModelForm(forms.ModelForm):
    class Meta(object):
        model = Edificio
        fields = ['nome', 'rua', 'numero', 'complemento', 'cidade',]

class ApartamentoModelForm(forms.ModelForm):
    class Meta(object):
        model = Apartamento
        fields = ['titulo', 'edificio', 'preco', 'descricao', 'imagem', 'numero_quartos', 'numero_banheiros',]

from django.contrib import admin
from .models import Cliente, Apartamento, Edificio

@admin.register(Edificio)
class EdificioAdmin(admin.ModelAdmin):
    lis_display = ('id', 'nome', 'rua', 'numero', 'complemento', 'cidade', 'pais', 'cep')

@admin.register(Apartamento)
class ApartamentoAdmin(admin.ModelAdmin):
    list_display = ('id', 'titulo', 'edificio', 'preco', 'imagem') # 'cliente',

@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('id','nome', 'sobrenome', 'email', 'telefone', 'cpf')

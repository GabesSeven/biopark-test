from django.db import models
from stdimage.models import StdImageField

# SIGNALS
from django.db.models import signals
from django.template.defaultfilters import slugify

# class Base(models.Model):
#     criado = models.DateField('Data de Criação', auto_now_add=True)
#     modificado = models.DateField('Data de Atualização', auto_now=True)
#     ativo = models.BooleanField('Ativo?', default=True)
#
#     class Meta:
#         abstract = True

class Cliente(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField('Nome', max_length=25)
    sobrenome = models.CharField('Sobrenome', max_length=25)
    email = models.EmailField('E-mail', max_length=100)
    telefone = models.CharField('Telefone', max_length=16, help_text='Máximo 16 caracteres')
    cpf = models.CharField('CPF', max_length=16, help_text='Máximo 16 caracteres')
    apartamento = models.ForeignKey('Apartamento', on_delete=models.CASCADE)


    class Meta():
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'

    def __str__(self):
        return f'{self.nome} {self.sobrenome}'

class Edificio(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField('Nome', max_length=50) # , help_text
    rua = models.CharField('Rua', max_length=50) # , help_text
    numero = models.IntegerField('Numero') # , help_text
    complemento = models.CharField('Complemento', max_length=100) # , help_text
    cidade = models.CharField('Cidade', max_length=100) # , help_text
    pais = models.CharField('País', max_length=100) # , help_text
    cep = models.CharField('CEP', max_length=100) # , help_text

    class Meta():
        verbose_name = 'Edificío'
        verbose_name_plural = 'Edificíos'

    def __str__(self):
        return self.nome

class Apartamento(models.Model):
    id = models.AutoField(primary_key=True)
    titulo = models.CharField('Título', max_length=50 , help_text='Máximo 50 caracteres')
    edificio  = models.ForeignKey('Edificio', on_delete=models.CASCADE)
    preco = models.DecimalField('Preço', max_digits=8, decimal_places=2, help_text='Valor mensal do imóvel')
    imagem = StdImageField('Imagem', upload_to='cadastros', variations={'thumb': (124, 124)})
    slug = models.SlugField('Slug', max_length=100, blank=True, editable=False)

    class Meta():
        verbose_name = 'Apartamento'
        verbose_name_plural = 'Apartamentos'

    def __str__(self):
        return self.titulo

def apartamento_pre_save(signal, instance, sender, **kwargs):
    instance.slug = slugify(instance.titulo)

signals.pre_save.connect(apartamento_pre_save, sender=Apartamento)

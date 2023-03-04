from django.db import models
from stdimage.models import StdImageField
from cpf_field.models import CPFField
from phonenumber_field.modelfields import PhoneNumberField

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
    telefone = PhoneNumberField(region="BR")
    cpf = CPFField('CPF')
    apartamento = models.ForeignKey('Apartamento', on_delete=models.CASCADE)

    class Meta():
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'

    def __str__(self):
        return f'{self.nome} {self.sobrenome}'

class Edificio(models.Model):

    CIDADE_CHOICES = (
        'Curitiba',
        'Londrina',
        'Maringá',
        'Ponta Grossa',
        'Cascavel',
        'São José dos Pinhais',
        'Foz do Iguaçu',
        'Colombo',
        'Guarapuava',
        'Paranaguá',
        'Araucária',
        'Toledo',
        'Apucarana',
        'Campo Largo',
        'Pinhais',
        'Arapongas',
    )

    id = models.AutoField(primary_key=True)
    nome = models.CharField('Nome', max_length=50)
    rua = models.CharField('Rua', max_length=50)
    numero = models.IntegerField('Número')
    complemento = models.CharField('Complemento', max_length=100)
    cidade = models.CharField('Cidade', max_length=50) # , choices=CIDADE_CHOICES

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
    descricao = models.TextField('Descrição')
    numero_quartos = models.IntegerField('Número de quartos') # , help_text
    numero_banheiros = models.IntegerField('Número de banheiros') # , help_text
    imagem = StdImageField('Imagem', upload_to='cadastros', variations={'thumb': (280, 280)})
    slug = models.SlugField('Slug', max_length=100, blank=True, editable=False)
    alugado = models.BooleanField('Alugado', default=False)

    class Meta():
        verbose_name = 'Apartamento'
        verbose_name_plural = 'Apartamentos'

    def __str__(self):
        return self.titulo

def apartamento_pre_save(signal, instance, sender, **kwargs):
    instance.slug = slugify(instance.titulo)

signals.pre_save.connect(apartamento_pre_save, sender=Apartamento)

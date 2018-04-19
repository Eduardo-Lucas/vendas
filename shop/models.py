from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True, unique=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name


class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=True, related_name='products')
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True)
    image = models.ImageField(upload_to='products/%Y/%m/%d', blank=True)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField()
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-created',)
        index_together = (('id', 'slug'),)

    def __str__(self):
        return self.name


FISICA_JURIDICA_CHOICES = (('F', 'Pessoa Física'), ('J', 'Pessoa Jurídica'))


class FormaPagamento(models.Model):
    sigla = models.CharField(max_length=3)
    descricaoPagamento = models.CharField(max_length=60)

    class Meta:
        ordering = ('sigla',)

    def __str__(self):
        return self.descricaoPagamento


class PrazoPagamento(models.Model):
    descricaoPrazoPagamento = models.CharField(max_length=60)

    class Meta:
        ordering = ('descricaoPrazoPagamento',)

    def __str__(self):
        return self.descricaoPrazoPagamento


class Cliente(models.Model):
    codigo = models.IntegerField()
    razaoSocial = models.CharField(max_length=60)
    nomeFantasia = models.CharField(max_length=60)
    tipo = models.CharField(max_length=1, choices=FISICA_JURIDICA_CHOICES, default='F')
    cnpjcpf = models.CharField(max_length=14, blank=True, null=True)
    inscricao = models.CharField(max_length=9, blank=True, null=True)
    regiao = models.CharField(max_length=14, blank=True, null=True)
    grupo = models.CharField(max_length=14, blank=True, null=True)
    # codigoVendedor = models.CharField(max_length=14, blank=True, null=True)
    endereco = models.CharField(max_length=60, blank=True, null=True)
    complemento = models.CharField(max_length=60, blank=True, null=True)
    bairro = models.CharField(max_length=60, blank=True, null=True)
    cidade = models.CharField(max_length=60, blank=True, null=True)
    cep = models.CharField(max_length=9, blank=True, null=True)
    uf = models.CharField(max_length=2, blank=True, null=True)
    telefone1 = models.CharField(max_length=20, blank=True, null=True)
    telefone2 = models.CharField(max_length=20, blank=True, null=True)
    telefoneCelular = models.CharField(max_length=20, blank=True, null=True)
    tipoPagamento = models.CharField(max_length=2, blank=True, null=True)
    vencimento = models.DateField(max_length=10, blank=True, null=True)
    limiteCreditoPedido = models.DecimalField(max_length=16, max_digits=16, decimal_places=2, blank=True, null=True)
    limiteGeralCredito = models.DecimalField(max_length=16, max_digits=16, decimal_places=2, blank=True, null=True)
    status = models.CharField(max_length=1, blank=True, null=True)
    justificaBloqueio = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        ordering = ('razaoSocial',)

    def __str__(self):
        return 'Cliente {}'.format(self.razaoSocial)




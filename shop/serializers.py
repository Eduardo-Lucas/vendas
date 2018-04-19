from rest_framework import serializers
from shop.models import Category, Product, FormaPagamento, PrazoPagamento, Cliente


class CategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Category
        fields = ('url', 'name', 'slug', 'products')


class ProductSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Product
        fields = ('url', 'category', 'name', 'slug', 'image', 'description', 'price', 'stock', 'available', 'created',
                  'updated')


class FormaPagamentoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = FormaPagamento
        fields = ('url', 'sigla', 'descricaoPagamento', 'pedidos')


class PrazoPagamentoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = PrazoPagamento
        fields = ('url', 'descricaoPrazoPagamento', 'pedidos')


class ClienteSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Cliente
        fields = ('url', 'codigo', 'razaoSocial', 'nomeFantasia', 'tipo', 'cnpjcpf', 'inscricao', 'regiao', 'grupo',
                  'endereco', 'complemento', 'bairro', 'cidade', 'cep', 'uf', 'telefone1', 'telefone2',
                  'telefoneCelular', 'tipoPagamento', 'vencimento', 'limiteCreditoPedido', 'limiteGeralCredito',
                  'status', 'justificaBloqueio', 'pedidos')

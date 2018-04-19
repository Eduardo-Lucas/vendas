from rest_framework import viewsets

from shop.models import Category, Product, FormaPagamento, PrazoPagamento, Cliente
from shop.serializers import CategorySerializer, ProductSerializer, FormaPagamentoSerializer, \
    PrazoPagamentoSerializer, ClienteSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    """
    Recurso que permite visualizar ou editar as Categorias.
    """
    queryset = Category.objects.all().order_by('name')
    serializer_class = CategorySerializer


class ProductViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows products to be viewed or edited.
    """
    queryset = Product.objects.all().order_by('name')
    serializer_class = ProductSerializer


class FormaPagamentoViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows formas de pagamento to be viewed or edited.
    """
    queryset = FormaPagamento.objects.all().order_by('sigla')
    serializer_class = FormaPagamentoSerializer


class PrazoPagamentoViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows prazos de pagamento to be viewed or edited.
    """
    queryset = PrazoPagamento.objects.all().order_by('sigla')
    serializer_class = PrazoPagamentoSerializer


class ClienteViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows clientes to be viewed or edited.
    """
    queryset = Cliente.objects.all().order_by('sigla')
    serializer_class = ClienteSerializer




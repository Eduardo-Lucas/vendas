from shop.views import CategoryViewSet, ProductViewSet, FormaPagamentoViewSet, PrazoPagamentoViewSet, ClienteViewSet

routeList = (
    (r'categories', CategoryViewSet),
    (r'products', ProductViewSet),
    (r'formaspagamentos', FormaPagamentoViewSet),
    (r'prazospagamentos', PrazoPagamentoViewSet),
    (r'clientes', ClienteViewSet),
)

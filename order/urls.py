from order.views import OrderViewSet, OrderItemViewSet

routeList = (
    (r'pedidos', OrderViewSet),
    (r'itenspedidos', OrderItemViewSet),
)

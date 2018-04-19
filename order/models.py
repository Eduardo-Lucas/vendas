from django.db import models

from shop.models import Cliente, FormaPagamento, PrazoPagamento, Product


class Order(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, blank=True, null=True, verbose_name="Cliente ",
                                related_name='pedidos')
    formapagamento = models.ForeignKey(FormaPagamento, on_delete=models.CASCADE, blank=True, null=True,
                                       verbose_name="Forma de Pagamento ", related_name='pedidos')
    prazopagamento = models.ForeignKey(PrazoPagamento, on_delete=models.CASCADE, blank=True, null=True,
                                       verbose_name="Prazo de Pagamento ", related_name='pedidos')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-created',)
        verbose_name = "pedido"
        verbose_name_plural = "pedidos"

    def __str__(self):
        return 'Order {}'.format(self.id)

    def get_total_cost(self):
        return sum(item.get_cost() for item in self.items.all())


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='order_items')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return '{}'.format(self.id)

    def get_cost(self):
        return self.price * self.quantity

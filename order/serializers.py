from rest_framework import serializers

from order.models import Order, OrderItem


class OrderSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Order
        fields = ('url', 'cliente', 'formapagamento', 'prazopagamento', 'created', 'updated', 'items')


class OrderItemSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = OrderItem
        fields = ('url', 'order', 'product', 'price', 'quantity')

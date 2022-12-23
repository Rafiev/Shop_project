from rest_framework import serializers

from applications.order.tasks import send_confirmation_email
from applications.order.models import Order


class OrderSerializer(serializers.ModelSerializer):
    owner = serializers.EmailField(required=False)

    class Meta:
        model = Order
        fields = '__all__'
        # exclude

    def create(self, validated_data):
        amount = validated_data['amount']
        product = validated_data['product']
        if amount > product.amount:
            raise serializers.ValidationError('В наличии нет такого количества!')
        if amount == 0:
            raise serializers.ValidationError('Необходимо заказать минимум один товаар')
        product.amount -= amount
        product.save(update_fields=['amount'])
        order = Order.objects.create(**validated_data)
        send_confirmation_email(order.owner.email, order.activation_code, order.product.title, order.total_cost)
        return order
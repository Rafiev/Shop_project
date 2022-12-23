import uuid

from django.contrib.auth import get_user_model
from django.db import models

from applications.product.models import Product

User = get_user_model()


class Order(models.Model):
    ORDER_STATUS = (
        ('in_processing', 'in_processing'),
        ('completed', 'completed'),
        ('declined', 'declined'),
    )
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='orders')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='orders')
    status = models.CharField(max_length=30, choices=ORDER_STATUS, null=True, blank=True)
    is_confirm = models.BooleanField(default=False)
    amount = models.PositiveIntegerField()
    address = models.TextField()
    number = models.CharField(max_length=30)
    total_cost = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    activation_code = models.UUIDField(default=uuid.uuid4)

    def save(self, *args, **kwargs):
        self.total_cost = self.amount * self.product.price
        return super().save(*args, **kwargs)
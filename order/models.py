from django.db import models
from django.contrib.auth.models import User

from product.models import Product

# Create your models here.
class Order(models.Model):
    orderId = models.IntegerField(unique=True)
    customer = models.ForeignKey(User, related_name="orders", on_delete = models.CASCADE)
    product = models.ForeignKey(Product, related_name="orders", on_delete =models.CASCADE)
    Quantity = models.IntegerField()
    amount = models.IntegerField()
    total_amount = models.IntegerField()
    payment = models.BooleanField(default=False)
    
    def save(self, *args, **kwargs):
        if not self.orderId:  # If orderId is not set
            last_order = Order.objects.last()
            if last_order:
                self.orderId = last_order.orderId + 20240
            else:
                self.orderId = 1  # Initial orderId
        super(Order, self).save(*args, **kwargs)
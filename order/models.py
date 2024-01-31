from django.db import models
from django.contrib.auth.models import User

from product.models import Product

# Create your models here.
class Order(models.Model):
    orderId = models.IntegerField()
    customer = models.ForeignKey(User, related_name="orders", on_delete = models.CASCADE)
    product = models.ForeignKey(Product, related_name="orders", on_delete =models.CASCADE)
    Quantity = models.IntegerField()
    amount = models.IntegerField()
    total_amount = models.IntegerField()
    payment = models.BooleanField(default=False)
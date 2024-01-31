from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class BillingDetails(models.Model):
    user = models.ForeignKey(User, related_name="billings", on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    company_name = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    town_or_city = models.CharField(max_length=150)
    country = models.CharField(max_length=100)
    postcode = models.CharField(max_length=50)
    mobile = models.CharField(max_length=11)
    email = models.EmailField(max_length=100)
    order_note = models.CharField(max_length=100, null= True, blank=True)
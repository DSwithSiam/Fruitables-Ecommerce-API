from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=80)
    
    def __str__(self):
        return self.name

class Additional(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=80)

    def __str__(self):
            return self.name

CHECK_CHOICES = [
        ('Healthy', 'Healthy'),
        ('Unhealthy', 'Unhealthy'),
    ]

class Product(models.Model):
    title = models.CharField(max_length=150)
    image = models.ImageField(upload_to='images/product/')
    price = models.IntegerField()
    category = models.ForeignKey(Category, null=True ,on_delete=models.SET_NULL, related_name="product",)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="product")
    description = models.TextField()
    weight = models.IntegerField()
    min_weight = models.IntegerField()
    country_of_origin = models.CharField(max_length=100)
    quality = models.ManyToManyField(Additional)
    chek = models.CharField(max_length=50, choices=CHECK_CHOICES)
    
    def __str__(self):
            return f"author: {self.author.username}, title: {self.title}, category: {self.category}"
    
    
class Review(models.Model):
    product = models.ForeignKey(Product, on_delete = models.CASCADE, related_name="review")
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    text = models.TextField()
    
    def __str__(self):
        return f"Product {self.product.title}, Name: {self.name}, Text: {self.text}"
    


RATEING_CHOICES = [
        ('1', '⭐'),
        ('2', '⭐⭐'),
        ('3', '⭐⭐⭐'),
        ('4', '⭐⭐⭐⭐'),
        ('5', '⭐⭐⭐⭐⭐'),
    ]


class Rateing(models.Model):
    product = models.ForeignKey(Product, on_delete = models.CASCADE, related_name="rateing")
    rateing = models.CharField(max_length=100, choices=RATEING_CHOICES) 

    
class Add_to_card(models.Model):
    orderId = models.IntegerField()
    customer = models.ForeignKey(User, related_name="add_to_card", on_delete = models.CASCADE)
    product = models.ForeignKey(Product, related_name="add_to_card", on_delete =models.CASCADE)
    Quantity = models.IntegerField()
    amount = models.IntegerField()
    total_amount = models.IntegerField()

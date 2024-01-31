from django.shortcuts import render
from rest_framework import viewsets
# Create your views here.
from . import models
from . import serializers

class CategoryViewset(viewsets.ModelViewSet):
    queryset = models.Category.objects.all()
    serializer_class = serializers.CategorySerializer
    
class AdditionalViewset(viewsets.ModelViewSet):
    queryset = models.Additional.objects.all()
    serializer_class = serializers.AdditionalSerializer
    
class ProductViewset(viewsets.ModelViewSet):
    queryset = models.Product.objects.all()
    serializer_class = serializers.ProductSerializer
    
class ReviewViewset(viewsets.ModelViewSet):
    queryset = models.Review.objects.all()
    serializer_class = serializers.ReviewSerializer
    
class RateingViewset(viewsets.ModelViewSet):
    queryset = models.Rateing.objects.all()
    serializer_class = serializers.RateingSerializer
    
class AddToCardViewset(viewsets.ModelViewSet):
    queryset = models.Add_to_card.objects.all()
    serializer_class = serializers.AddToCardSerializer

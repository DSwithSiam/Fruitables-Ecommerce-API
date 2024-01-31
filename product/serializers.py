from rest_framework import serializers

from product.models import *

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class AdditionalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Additional
        fields = '__all__'

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'

class RateingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rateing
        fields = '__all__'


class AddToCardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Add_to_card
        fields = ['orderId', 'customer', 'product', 'Quantity', 'amount', 'total_amount']

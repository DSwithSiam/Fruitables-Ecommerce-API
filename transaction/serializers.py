from rest_framework import serializers
from .models import BillingDetails 




class BillingDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = BillingDetails
        fields = '__all__'

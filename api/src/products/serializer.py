from rest_framework import serializers
from rest_framework.fields import ReadOnlyField
from .models.models import Products

class ProductSerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=50, min_length=2, required=True)
    price = serializers.FloatField(min_value=1, required=True)
    class Meta:
        model = Products
        fields = '__all__'
        
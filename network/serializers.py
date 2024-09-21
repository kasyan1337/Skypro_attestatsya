from rest_framework import serializers

from .models import NetworkNode, Product


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class NetworkNodeSerializer(serializers.ModelSerializer):
    products = ProductSerializer(many=True ,read_only=True)
    supplier = serializers.StringRelatedField() # supplier = serializers.StringRelatedField() shows the supplier’s name

    class Meta:
        model = NetworkNode
        fields = '__all__'
        read_only_fields = ('debt', 'created_at') # prevents debt from being updated via the API

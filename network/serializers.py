from rest_framework import serializers

from .models import Product, NetworkNode


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class NetworkNodeSerializer(serializers.ModelSerializer):
    products = ProductSerializer(many=True, read_only=True)
    supplier = serializers.PrimaryKeyRelatedField(
        queryset=NetworkNode.objects.all(), allow_null=True
    )
    supplier_name = serializers.CharField(
        source='supplier.name', read_only=True
    )  # Optional: Display supplier's name in responses

    class Meta:
        model = NetworkNode
        fields = '__all__'
        read_only_fields = ('debt', 'created_at')  # prevents debt from being updated via the API

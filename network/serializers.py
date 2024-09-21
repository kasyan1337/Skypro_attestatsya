from rest_framework import serializers

from .models import Product, NetworkNode


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class NetworkNodeSerializer(serializers.ModelSerializer):
    products = serializers.PrimaryKeyRelatedField(
        many=True, queryset=Product.objects.all(), required=False
    )
    supplier = serializers.PrimaryKeyRelatedField(
        queryset=NetworkNode.objects.all(), allow_null=True, required=False
    )
    supplier_name = serializers.CharField(
        source='supplier.name', read_only=True
    )

    def validate_supplier(self, value):
        if self.instance and self.instance.level == 0 and value is not None:
            raise serializers.ValidationError("Supplier must be null for level 0 nodes.")
        return value

    class Meta:
        model = NetworkNode
        fields = '__all__'
        read_only_fields = ('created_at',)
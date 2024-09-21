from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets

from network.models import NetworkNode
from network.serializers import NetworkNodeSerializer, ProductSerializer
from .permissions import IsActiveStaff


# Create your views here.
class ProductViewSet(viewsets.ModelViewSet):
    queryset = NetworkNode.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsActiveStaff]
class NetworkNodeViewSet(viewsets.ModelViewSet):
    queryset = NetworkNode.objects.all()
    serializer_class = NetworkNodeSerializer
    permission_classes = [IsActiveStaff]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['country']  # enables filtering via query parameters

    def create(self, request, *args, **kwargs):
        print(request.data)
        response = super().create(request, *args, **kwargs)
        return response

    def get_queryset(self):
        return super().get_queryset().select_related('supplier').prefetch_related(
            'products')  # reduces the number of queries

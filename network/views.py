from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets

from network.models import NetworkNode
from network.serializers import NetworkNodeSerializer
from .permissions import IsActiveStaff


# Create your views here.

class NetworkNodeViewSet(viewsets.ModelViewSet):
    queryset = NetworkNode.objects.all()
    serializer_class = NetworkNodeSerializer
    permission_classes = [IsActiveStaff]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['country']  # enables filtering via query parameters

    def get_queryset(self):
        return super().get_queryset().select_related('supplier').prefetch_related(
            'products')  # reduces the number of queries

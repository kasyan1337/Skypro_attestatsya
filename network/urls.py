from django.urls import path, include
from rest_framework.routers import DefaultRouter

from network.views import NetworkNodeViewSet

router = DefaultRouter()
router.register(r'network-nodes', NetworkNodeViewSet)

urrpatterns = [
    path('', include(router.urls)),
]

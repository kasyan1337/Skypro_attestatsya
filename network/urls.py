from rest_framework.routers import DefaultRouter

from network.views import NetworkNodeViewSet, ProductViewSet

router = DefaultRouter()
router.register(r'network-nodes', NetworkNodeViewSet, basename='networknode')
router.register(r'products', ProductViewSet, basename='product')

urlpatterns = router.urls
#
# urlpatterns = [
#     path('', include(router.urls)),
# ]

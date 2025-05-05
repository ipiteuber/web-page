from rest_framework import viewsets, permissions
from core.models import Product
from .serializers import ProductSerializer

class AvailableProductViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Product.objects.filter(stock__gt=0)
    serializer_class = ProductSerializer
    authentication_classes = []
    permission_classes = [permissions.AllowAny]

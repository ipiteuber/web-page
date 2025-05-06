from rest_framework import viewsets, permissions
from core.models import Product
from .serializers import ProductSerializer
from rest_framework.authentication import TokenAuthentication

class AvailableProductViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Product.objects.filter(stock__gt=0)
    serializer_class = ProductSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes     = [permissions.IsAuthenticated]

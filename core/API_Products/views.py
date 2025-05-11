from rest_framework import viewsets, permissions
from core.models import Product
from .serializers import ProductSerializer
from rest_framework.authentication import TokenAuthentication
from drf_yasg.utils import swagger_auto_schema

class AvailableProductViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Product.objects.filter(stock__gt=0)
    serializer_class = ProductSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes     = [permissions.IsAuthenticated]

    @swagger_auto_schema(operation_description="Available products", responses={200: ProductSerializer(many=True)})
    def list(self, request, *args, **kwargs):
        """
        Gets the list of products in stock.
        Only accessible to authenticated users.
        """
        return super().list(request, *args, **kwargs)
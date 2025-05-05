from rest_framework.routers import DefaultRouter
from .views import AvailableProductViewSet

router = DefaultRouter()
router.register(r'available', AvailableProductViewSet, basename='available-products')

urlpatterns = router.urls

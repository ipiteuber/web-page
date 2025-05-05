from rest_framework.routers import DefaultRouter
from .views import CoachAdminViewSet

router = DefaultRouter()
router.register(r'admin', CoachAdminViewSet, basename='coach-admin')

urlpatterns = router.urls

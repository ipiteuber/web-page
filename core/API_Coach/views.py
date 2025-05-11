from django.shortcuts import render
from rest_framework.authentication import TokenAuthentication
from rest_framework import viewsets, permissions
from core.models import Coach
from core.API_Coach.serializers import CoachSerializer
from drf_yasg.utils import swagger_auto_schema

# Create your views here.

class IsStaff(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.is_staff

class CoachAdminViewSet(viewsets.ModelViewSet):
    """
    CRUD Coach solo accesible por staff
    """
    queryset = Coach.objects.all()
    serializer_class = CoachSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsStaff]

    @swagger_auto_schema(operation_description="Coaches List")
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @swagger_auto_schema(operation_description="New Coach")
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)
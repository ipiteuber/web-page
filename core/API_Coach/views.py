from django.shortcuts import render
from rest_framework.authentication import TokenAuthentication
from rest_framework import viewsets, permissions
from core.models import Coach
from core.API_Coach.serializers import CoachSerializer

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

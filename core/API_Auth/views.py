from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.authtoken.models import Token
from .serializers import RegisterSerializer
from drf_yasg.utils import swagger_auto_schema

class RegisterUserView(APIView):
    permission_classes = [AllowAny]

    @swagger_auto_schema(operation_description="Register a new user", request_body=RegisterSerializer, responses={201: 'Usuario creado', 400: 'Datos inválidos'})
    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        user = serializer.save()
        token, _ = Token.objects.get_or_create(user=user)
        return Response({'token': token.key}, status=status.HTTP_201_CREATED)
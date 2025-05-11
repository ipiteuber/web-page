from rest_framework import serializers
from django.contrib.auth import get_user_model
from core.models import Role, UserRole

User = get_user_model()

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    class Meta:
        model = User
        fields = ['fullname', 'username', 'email', 'idnumber', 'datebirth', 'phone', 'password']

    def create(self, validated_data):
        # Crear usuario y hashear contraseña
        password = validated_data.pop('password')
        user = User(**validated_data)
        user.set_password(password)
        user.save()

        # Asignar rol "client" por defecto
        try:
            client_role = Role.objects.get(role_name='client')
            UserRole.objects.create(user=user, role=client_role)
        except Role.DoesNotExist:
            # Aquí puedes crearlo automáticamente o ignorar
            pass

        return user

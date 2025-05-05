from rest_framework import serializers
from core.models import Coach

class CoachSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)  # Muestra el username

    class Meta:
        model = Coach
        fields = ['id', 'nickname', 'fullname', 'bio', 
                'total_sessions', 'created_at', 'updated_at']
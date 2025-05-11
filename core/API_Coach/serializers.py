from rest_framework import serializers
from core.models import Coach

class CoachSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coach
        fields = ['id', 'user', 'nickname', 'fullname', 'bio', 'total_sessions', 'created_at', 'updated_at']
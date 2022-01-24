import imp
from rest_framework import serializers
from .models import Drawing
from user.serializer import UserSerializer

class DrawingSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    class Meta:
        model = Drawing
        fields = (
            'id', 
            'title', 
            'is_public', 
            'json_data', 
            'created_at', 
            'updated_at',
            'user',
            'user_id'
        )
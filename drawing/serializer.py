from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Drawing



class UserSerializer(serializers.ModelSerializer):
    """ A serializer class for the User model """
    class Meta:
        model = User
        fields = (
            'id', 
            'username',
            # 'email'
            'is_active', 
            'is_superuser'
        )

class DrawingSerializer(serializers.ModelSerializer):
    # user = UserSerializer()
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
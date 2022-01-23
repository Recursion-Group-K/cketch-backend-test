from rest_framework import serializers
from .models import Drawing

class DrawingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Drawing
        fields = (
            'id', 
            'title', 
            'is_public', 
            'json_data', 
            'created_at', 
            'updated_at'
        )
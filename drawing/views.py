from django.shortcuts import render
from rest_framework import viewsets
from .models import Drawing
from .serializer import DrawingSerializer

class DrawingViewSet(viewsets.ModelViewSet):
    queryset = Drawing.objects.all()
    serializer_class = DrawingSerializer
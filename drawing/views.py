from django.contrib.auth.models import User
from rest_framework import viewsets, generics, permissions
from .models import Drawing
from .serializer import DrawingSerializer, UserSerializer
from django.contrib.auth.hashers import make_password

""" Drawing View """
class DrawingViewSet(viewsets.ModelViewSet):
    queryset = Drawing.objects.all()
    serializer_class = DrawingSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    filter_fields = ['user']

""" User View """
class UserList(generics.ListAPIView):
    """ View to list all users"""
    queryset = User.objects.all().order_by('first_name')
    serializer_class = UserSerializer
    permission_classes = (permissions.IsAuthenticated,)


class UserCreate(generics.CreateAPIView):
    """ View to create a new user. Only accepts POST requests """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (permissions.IsAdminUser, )

    def perform_create(self, serializer):
        data = serializer.data
        password = data.pop('password', 'something')
        user = User(password=make_password(password), **data)
        user.save()
        return user


class UserRetrieveUpdate(generics.RetrieveUpdateAPIView):
    """ Retrieve a user or update user information.
    Accepts GET and PUT requests and the record id must be provided in the request """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (permissions.IsAuthenticated, )
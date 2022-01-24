from django.urls import path, include
from rest_framework import routers
from .views import *

router = routers.DefaultRouter()
router.register(r'drawings', DrawingViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('users/', UserList.as_view()),
    path('create-users/', UserCreate.as_view()),
    path('users/<pk>/', UserRetrieveUpdate.as_view()),
]

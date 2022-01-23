from rest_framework import routers
from .views import DrawingViewSet

router = routers.DefaultRouter()
router.register(r'drawing', DrawingViewSet)
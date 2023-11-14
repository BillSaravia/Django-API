from rest_framework import routers

from .viewsets import UserViewSet

app_name = "sistema"

router = routers.DefaultRouter()
router.register('Users',UserViewSet)

from django.contrib.auth.models import User

from rest_framework import viewsets, mixins

from .serializers import UserSerializer

from .permissions import IsUserOwnerOrGetAndPostOnly

from .models import Profile


class UserViewSet(viewsets.ModelViewSet):
    permission_classes = [IsUserOwnerOrGetAndPostOnly, ]
    queryset = User.objects.all()
    serializer_class = UserSerializer


from users.models import User
from rest_framework.response import Response
from users.serializers import UserProfileSerializer
from rest_framework import viewsets
from rest_framework.permissions import (AllowAny, IsAuthenticated)
from users.permissions import IsLoggedInUserOrAdmin, IsAdminUser
from rest_framework.views import APIView

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserProfileSerializer

    def get_permissions(self):
        permission_classes = []
        if self.action == 'create':
            permission_classes = [AllowAny]
        elif self.action == 'retrieve' or self.action == 'update' or self.action == 'patch':
            permission_classes = [IsLoggedInUserOrAdmin]
        elif self.action == 'list' or self.action == 'destroy':
            permission_classes = [IsAdminUser]
        return [permission() for permission in permission_classes]

class Indexview(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        content = { 'message' : 'Welcome to Flexy'}
        return Response(content)
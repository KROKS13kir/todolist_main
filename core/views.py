# Create your views here.
from django.contrib.auth import authenticate, login, logout
from rest_framework.generics import CreateAPIView, RetrieveUpdateDestroyAPIView, UpdateAPIView
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response

from core.models import User
from .serializers import SignUpSerializer, LoginSerializer, RetrieveUpdateSerializer, PasswordUpdateSerializer


class SignUpView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = SignUpSerializer
    permission_classes = [AllowAny]


class LoginView(CreateAPIView):
    serializer_class = LoginSerializer

    def post(self, request, *args, **kwargs):
        serializer: LoginSerializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        login(request, user=user)
        user_serializer = RetrieveUpdateSerializer(instance=user)
        return Response(user_serializer.data)


class UserRetrieveUpdateView(RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = RetrieveUpdateSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return self.request.user

    def delete(self, request, *args, **kwargs):
        logout(request)
        return Response({})


class PasswordUpdateView(UpdateAPIView):
    queryset = User.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = PasswordUpdateSerializer

    def get_object(self):
        return self.request.user

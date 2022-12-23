# Create your views here.
from django.contrib.auth import authenticate, login, logout
from django.contrib.sites import requests
from rest_framework.generics import CreateAPIView, RetrieveUpdateDestroyAPIView, UpdateAPIView
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response

from core.models import User
from core.serializers import LoginSerializer, RetrieveUpdateSerializer, PasswordUpdateSerializer, SignUpSerializer


class SignUpView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = SignUpSerializer
    permission_classes = [AllowAny]


class LoginView(CreateAPIView):
    serializer_class = LoginSerializer

    def post(self, request: requests, *args: str, **kwargs: int) -> Response:
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

    def get_object(self) -> User:
        return self.request.user

    def delete(self, request: requests, *args: str, **kwargs: int) -> Response:
        """
        При выходе из профиля, пользователь не должен удалятся из бд.
        """
        logout(request)
        return Response({})


class PasswordUpdateView(UpdateAPIView):
    queryset = User.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = PasswordUpdateSerializer

    def get_object(self) -> User:
        return self.request.user

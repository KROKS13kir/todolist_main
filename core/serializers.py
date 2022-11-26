from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from .models import User


class SignUpSerializer(serializers.ModelSerializer):
    username = serializers.CharField(
        max_length=150,
        validators=[
            UniqueValidator(queryset=User.objects.all())
        ]
    )
    password = serializers.CharField(min_length=1, write_only=True, validators=[validate_password])
    password_repeat = serializers.CharField(min_length=1, write_only=True, validators=[validate_password])

    class Meta:
        model = User
        fields = [
            'id',
            'username',
            'email',
            'first_name',
            'last_name',
            'password',
            'password_repeat'
        ]

    def validate(self, attrs):
        """
        Переопределил пустой validate для проверки пароля, так же достаю и удаляю password_repeat.
        """
        password_repeat = attrs.pop('password_repeat', None)
        password = attrs.get('password')

        if password_repeat != password:
            raise ValidationError('Passwords do not match')
        return attrs

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(required=True)
    password = serializers.CharField(required=True)

    def validated_username(self, input):
        if not User.objects.filter(username=input).exists():
            raise serializers.ValidationError(["User with such username doesn't exist"])
        return input


class RetrieveUpdateSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    username = serializers.CharField(
        validators=[
            UniqueValidator(queryset=User.objects.all())
        ]
    )

    class Meta:
        model = User
        fields = (
            'id',
            'username',
            'first_name',
            'last_name',
            'email'
        )


class PasswordUpdateSerializer(serializers.Serializer):
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)

    def validate_new_password(self, input):
        validate_password(input)
        return input

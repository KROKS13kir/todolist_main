from rest_framework import serializers
from goals.models import Goal
from core.serializers import RetrieveUpdateSerializer


class GoalCreateSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Goal
        read_only_fields = ("id", "created", "updated", "user")
        fields = "__all__"


class GoalSerializer(serializers.ModelSerializer):
    user = RetrieveUpdateSerializer(read_only=True)

    class Meta:
        model = Goal
        read_only_fields = ("id", "created", "updated", "user")
        fields = "__all__"
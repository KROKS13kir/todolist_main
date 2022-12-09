from rest_framework import serializers
from core.serializers import RetrieveUpdateSerializer
from goals.models.board import BoardParticipant
from goals.models.goal import Goal


class GoalCreateSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Goal
        read_only_fields = ("id", "created", "updated", "user")
        fields = "__all__"

    def validate(self, attrs):
        roll = BoardParticipant.objects.filter(user=attrs.get('user'), board=attrs.get('board'), role__in=[BoardParticipant.Role.owner, BoardParticipant.Role.writer],).exists()
        if roll:
            return attrs
        raise serializers.Validation('You do not have permission to perform this action')



class GoalSerializer(serializers.ModelSerializer):
    user = RetrieveUpdateSerializer(read_only=True)

    class Meta:
        model = Goal
        read_only_fields = ("id", "created", "updated", "user")
        fields = "__all__"
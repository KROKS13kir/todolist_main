from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from core.serializers import RetrieveUpdateSerializer
from goals.models.board import BoardParticipant
from goals.models.goal import Goal


class GoalCreateSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Goal
        fields = "__all__"
        read_only_fields = ("id", "created", "updated", "description", "user")

    def validate_category(self, value):
        if value.is_deleted:
            raise ValidationError("not allowed in deleted category")

        user = value.board.participants.filter(user=self.context["request"].user).first()
        if not user:
            raise ValidationError("not owner or writer in the related board")
        elif user.role not in [BoardParticipant.Role.owner, BoardParticipant.Role.writer]:
            raise ValidationError("not owner or writer in the related board")

        return value



class GoalSerializer(serializers.ModelSerializer):
    user = RetrieveUpdateSerializer(read_only=True)

    class Meta:
        model = Goal
        read_only_fields = ("id", "created", "updated", "user")
        fields = "__all__"
from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from core.serializers import RetrieveUpdateSerializer
from goals.models.board import BoardParticipant
from goals.models.category import Category


class CategoryCreateSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Category
        read_only_fields = ("id", "created", "updated", "user")
        fields = "__all__"

    # def validate(self, attrs):
    #     roll = BoardParticipant.objects.filter(
    #         user=attrs.get('user'),
    #         board=attrs.get('board'),
    #         role__in=[BoardParticipant.Role.owner, BoardParticipant.Role.writer],
    #     ).exists()
    #     if roll:
    #         return attrs
    #     raise ValidationError('You do not have permission to perform this action')


class CategorySerializer(serializers.ModelSerializer):
    user = RetrieveUpdateSerializer(read_only=True)

    class Meta:
        model = Category
        fields = "__all__"
        read_only_fields = ("id", "created", "updated", "user")

    def validate_category(self, value):
        if value.is_deleted:
            raise ValidationError('not allowed in deleted category')
        if value.user != self.context['request'].user:
            raise ValidationError('not owner of category')

        return value
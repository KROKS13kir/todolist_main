from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from core.serializers import RetrieveUpdateSerializer
from goals.models.board import BoardParticipant
from goals.models.comment import Comment


class CommentCreateSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Comment
        read_only_fields = ('id', 'user', 'created', 'updated', 'goal')
        fields = '__all__'

    def validate(self, attrs):
        roll = BoardParticipant.objects.filter(
            user=attrs.get('user'),
            board=attrs.get('board'),
            role__in=[BoardParticipant.Role.owner, BoardParticipant.Role.writer],
        ).exists()
        if roll:
            return attrs
        raise ValidationError('You do not have permission to perform this action')


class CommentSerializer(serializers.ModelSerializer):
    user = RetrieveUpdateSerializer(read_only=True)

    class Meta:
        model = Comment
        read_only_fields = ('id', 'user', 'created', 'updated', 'goal')
        fields = '__all__'

from rest_framework import serializers
from core.serializers import RetrieveUpdateSerializer
from goals.models.comment import Comment


class CommentCreateSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Comment
        read_only_fields = ('id', 'user', 'created', 'updated', 'goal')
        fields = '__all__'


class CommentSerializer(serializers.ModelSerializer):
    user = RetrieveUpdateSerializer(read_only=True)

    class Meta:
        model = Comment
        read_only_fields = ('id', 'user', 'created', 'updated', 'goal')
        fields = '__all__'

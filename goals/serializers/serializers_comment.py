from rest_framework import serializers
from goals.models import GoalComment
from core.serializers import RetrieveUpdateSerializer
from goals.serializers.serializers_goals import GoalCategorySerializer


class CommentCreateSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = GoalComment
        read_only_fields = ('id', 'user', 'created', 'updated', 'goal')
        fields = '__all__'

class CommentSerializer(serializers.ModelSerializer):
    user = RetrieveUpdateSerializer(read_only=True)
    goal = GoalCategorySerializer(read_only=True)

    class Meta:
        model = GoalComment
        read_only_fields = ('id', 'user', 'created', 'updated')
        fields = '__all__'


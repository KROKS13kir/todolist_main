from django.db import transaction
from django_filters.rest_framework.backends import DjangoFilterBackend
from rest_framework import permissions, filters
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.pagination import LimitOffsetPagination
from goals.filters import GoalDateFilter
from goals.models.board import Board
from goals.models.category import Category
from goals.models.comment import Comment
from goals.models.goal import Goal
from goals.permissions import GoalPermissions, CommentPermissions, CategoryPermissions, BoardPermissions
from goals.serializers.serializers_board import BoardCreateSerializer, BoardSerializer, BoardListSerializer
from goals.serializers.serializers_category import CategoryCreateSerializer, CategorySerializer
from goals.serializers.serializers_comment import CommentCreateSerializer, CommentSerializer
from goals.serializers.serializers_goals import GoalCreateSerializer, GoalSerializer


class GoalCreateView(CreateAPIView):
    model = Goal
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = GoalCreateSerializer


class GoalListView(ListAPIView):
    model = Goal
    permission_classes = [permissions.IsAuthenticated, GoalPermissions]
    serializer_class = GoalSerializer
    pagination_class = LimitOffsetPagination
    filter_backends = [
        DjangoFilterBackend,
        filters.OrderingFilter,
        filters.SearchFilter,
                       ]
    filterset_class = GoalDateFilter
    ordering_fields = ["priority", "due_date"]
    ordering = ["priority", "due_date"]
    search_fields = ["title"]

    def get_queryset(self) -> Goal:
        return Goal.objects.filter(
            category__board__participants__user=self.request.user
        )


class GoalView(RetrieveUpdateDestroyAPIView):
    model = Goal
    serializer_class = GoalSerializer
    permission_classes = [permissions.IsAuthenticated, GoalPermissions]

    def get_queryset(self) -> Goal:
        return Goal.objects.filter(
            category__board__participants__user=self.request.user
        )

    def perform_destroy(self, instance: Goal) -> Goal:
        instance.status = Goal.Status.archived
        instance.save()
        return instance


class CommentCreateView(CreateAPIView):
    model = Comment
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = CommentCreateSerializer

    def perform_create(self, serializer: CommentCreateSerializer) -> None:
        serializer.save(goal_id=self.request.data['goal'])


class CommentListView(ListAPIView):
    model = Comment
    permission_classes = [permissions.IsAuthenticated, CommentPermissions]
    serializer_class = CommentSerializer
    pagination_class = LimitOffsetPagination
    filter_backends = [filters.OrderingFilter, DjangoFilterBackend]
    filterset_fields = ["goal"]
    ordering = ["-id"]

    def get_queryset(self) -> Comment:
        return Comment.objects.filter(
            goal__category__board__participants__user=self.request.user
        )


class CommentView(RetrieveUpdateDestroyAPIView):
    model = Comment
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticated, CommentPermissions]

    def get_queryset(self) -> Comment:
        return Comment.objects.filter(
            goal__category__board__participants__user=self.request.user
        )

class GoalCategoryCreateView(CreateAPIView):
    model = Category
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = CategoryCreateSerializer


class GoalCategoryListView(ListAPIView):
    model = Category
    permission_classes = [permissions.IsAuthenticated, CategoryPermissions]
    serializer_class = CategorySerializer
    pagination_class = LimitOffsetPagination
    filter_backends = [
        DjangoFilterBackend,
        filters.OrderingFilter,
        filters.SearchFilter,
    ]
    filterset_fields = ["board", "user"]
    ordering_fields = ["title", "created"]
    ordering = ["title"]
    search_fields = ["title"]

    def get_queryset(self) -> Category:
        return Category.objects.filter(
            board__participants__user=self.request.user, is_deleted=False
        )


class GoalCategoryView(RetrieveUpdateDestroyAPIView):
    model = Category
    serializer_class = CategorySerializer
    permission_classes = [permissions.IsAuthenticated, CategoryPermissions]

    def get_queryset(self) -> Category:
        return Category.objects.filter(
            board__participants__user=self.request.user, is_deleted=False
        )

    def perform_destroy(self, instance: Category) -> Category:
        with transaction.atomic():
            instance.is_deleted = True
            instance.save()
            Goal.objects.filter(category=instance).update(status=Goal.Status.archived)
        return instance


class BoardCreateView(CreateAPIView):
    model = Board
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = BoardCreateSerializer


class BoardView(RetrieveUpdateDestroyAPIView):
    model = Board
    permission_classes = [permissions.IsAuthenticated, BoardPermissions]
    serializer_class = BoardSerializer

    def get_queryset(self) -> Board:
        return Board.objects.filter(participants__user=self.request.user, is_deleted=False)

    def perform_destroy(self, instance: Board) -> Board:
        with transaction.atomic():
            instance.is_deleted = True
            instance.save()
            instance.categories.update(is_deleted=True)
            Goal.objects.filter(category__board=instance).update(
                status=Goal.Status.archived
            )
        return instance


class BoardListView(ListAPIView):
    model = Board
    permission_classes = [permissions.IsAuthenticated]
    pagination_class = LimitOffsetPagination
    serializer_class = BoardListSerializer
    filter_backends = [
        filters.OrderingFilter,
    ]
    ordering = ["title"]

    def get_queryset(self) -> Board:
        return Board.objects.filter(participants__user=self.request.user, is_deleted=False)

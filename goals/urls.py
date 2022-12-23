from django.urls import path

from goals.views import GoalCategoryCreateView, GoalCategoryListView, GoalCategoryView, GoalCreateView, GoalListView, \
    GoalView, CommentCreateView, CommentListView, CommentView, BoardCreateView, BoardListView, BoardView

urlpatterns = [
    path("goal_category/create", GoalCategoryCreateView.as_view(), name='create_category'),
    path("goal_category/list", GoalCategoryListView.as_view(), name='list_category'),
    path("goal_category/<pk>", GoalCategoryView.as_view(), name='retrieve_category'),
    path("goal/create", GoalCreateView.as_view(), name='create_goal'),
    path("goal/list", GoalListView.as_view(), name='list_goal'),
    path("goal/<pk>", GoalView.as_view(), name='retrieve_goal'),
    path("goal_comment/create", CommentCreateView.as_view(), name='create_comment'),
    path("goal_comment/list", CommentListView.as_view(), name='list_comment'),
    path("goal_comment/<pk>", CommentView.as_view(), name='retrieve_comment'),
    path("board/create", BoardCreateView.as_view(), name='create_board'),
    path("board/list", BoardListView.as_view(), name='list_board'),
    path("board/<pk>", BoardView.as_view(), name='retrieve_board'),
]

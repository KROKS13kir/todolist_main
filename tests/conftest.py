import pytest as pytest
from rest_framework.test import APIClient

from goals.models.board import Board, BoardParticipant
from goals.models.category import Category
from goals.models.comment import Comment
from goals.models.goal import Goal
from core.models import User
from tests.factories import BoardFactory, BoardParticipantFactory, CategoryFactory, GoalFactory, CommentFactory


@pytest.fixture
def add_user(db) -> User:
    user = User.objects.create_user(
        username='lionel',
        email='lionel@gmail.com',
        password='SuperFootball2022_'
    )
    return user


@pytest.fixture
def auth_user(add_user: User) -> APIClient:
    client = APIClient()
    client.login(username='lionel', password='SuperFootball2022_')
    return client


@pytest.fixture
def board() -> Board:
    return BoardFactory.create()


@pytest.fixture
def board_participant(add_user: User, board: Board) -> BoardParticipant:
    return BoardParticipantFactory.create(user=add_user, board=board)


@pytest.fixture
def category(board: Board, add_user: User, board_participant: BoardParticipant) -> Category:
    return CategoryFactory.create(board=board, user=add_user)


@pytest.fixture
def goal(category: Category, add_user: User) -> Goal:
    return GoalFactory.create(user=add_user, category=category)


@pytest.fixture
def comment(goal: Goal, add_user: User) -> Comment:
    return CommentFactory.create(user=add_user, goal=goal)
import factory
from factory import fuzzy
from factory.declarations import SubFactory
from factory.faker import Faker
from goals.models.board import Board, BoardParticipant
from goals.models.category import Category
from goals.models.comment import Comment
from goals.models.goal import Goal
from core.models import User


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    username = Faker('name')
    email = Faker('email')
    password = 'strongPassword2022!'


class BoardFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Board

    title = fuzzy.FuzzyText(length=25)


class BoardParticipantFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = BoardParticipant

    board = SubFactory(BoardFactory)
    user = SubFactory(UserFactory)


class CategoryFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Category

    board = SubFactory(BoardFactory)
    title = fuzzy.FuzzyText(length=10)
    user = SubFactory(UserFactory)


class GoalFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Goal

    title = fuzzy.FuzzyText(length=10)
    user = SubFactory(UserFactory)
    category = SubFactory(CategoryFactory)


class CommentFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Comment

    text = fuzzy.FuzzyText(length=10)
    goal = SubFactory(UserFactory)
    user = SubFactory(GoalFactory)
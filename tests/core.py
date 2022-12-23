import pytest
from django.urls import reverse
from rest_framework.test import APIClient

from core.models import User
from serializers import RetrieveUpdateSerializer


@pytest.mark.django_db
def test_create(client: APIClient) -> None:
    data = {
        'username': 'lionel',
        'email': 'lionel@gmail.com',
        'password': 'SuperFootball2022_',
        'password_repeat': 'SuperFootball2022_',
    }
    response = client.post(
        reverse('signup'),
        data=data,
    )
    user = User.objects.order_by('-pk').first()
    expected_response = {
        'id': response.data.get('id'),
        'first_name': '',
        'last_name': '',
        'username': 'lionel',
        'email': 'lionel@gmail.com',
    }

    assert response.status_code == 201
    assert response.data == expected_response
    assert user.is_superuser is False


@pytest.mark.django_db
def test_login(client: APIClient, add_user: User) -> None:
    response = client.post(
        reverse('login'),
        data={
            'username': 'lionel',
            'password': 'SuperFootball2022_',
        },
        content_type='application/json',
    )

    assert response.status_code == 200





@pytest.mark.django_db
def test_profile(auth_user: APIClient, add_user: User) -> None:
    response = auth_user.get(reverse('profile'))
    expected_response = RetrieveUpdateSerializer(instance=add_user).data

    assert response.status_code == 200
    assert response.data == expected_response


@pytest.mark.django_db
def test_update_password(auth_user: APIClient, add_user: User) -> None:
    response = auth_user.put(
        reverse('update_password'),
        data={
            'new_password': 'SuperFootball2022_!!',
            'old_password': 'SuperFootball2022_',
        },
    )

    assert response.status_code == 200
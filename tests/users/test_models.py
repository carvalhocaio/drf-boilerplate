import pytest
from django.contrib.auth.models import User
from faker import Faker

from tests.factories import UserFactory

fake = Faker()


@pytest.mark.django_db
def test_create_user():
    user = UserFactory()

    assert isinstance(user, User)
    assert User.objects.filter(username=user.username).exists()


@pytest.mark.django_db
def test_create_multiple_user():
    for _ in range(10):
        user = fake.user_name()
        email = fake.email()
        password = fake.password()

        user = UserFactory(username=user, email=email, password=password)

        assert isinstance(user, User)
        assert User.objects.filter(username=user.username).exists()
        assert User.objects.filter(email=user.email).exists()

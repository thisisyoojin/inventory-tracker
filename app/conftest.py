from tracker.models import Item, Restaurant
from model_bakery import baker
import pytest
from django.contrib.auth.models import User
from django.test import Client


@pytest.fixture
def tester():
    return User.objects.create_superuser(
        username="tester",
        email="tester@mail.com",
        password="12345678"
    )


@pytest.fixture
def client(tester):
    client = Client()
    client.force_login(tester)
    return client


@pytest.fixture
def restaurant_a():
    return baker.make(Restaurant)


@pytest.fixture
def restaurant_b():
    return baker.make(Restaurant)


@pytest.fixture
def item_a(restaurant_a):
    return baker.make(Item, restaurant=restaurant_a)


@pytest.fixture
def item_b(restaurant_b):
    return baker.make(Item, restaurant=restaurant_b)

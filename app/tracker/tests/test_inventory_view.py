from tracker.models import Item, Restaurant
from model_bakery import baker
import pytest


@pytest.mark.django_db
class TestInventoryPage:
    def test_the_page_returns(self, client):
        response = client.get('/')
        assert response.status_code == 200

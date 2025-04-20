import pytest
from tracker.models import Inventory


@pytest.mark.django_db
class TestInventoryListAjax:
    def test_it_returns_items(self, client, item_a, item_b):
        response = client.get(f'/ajax/inventory_items')
        assert response.status_code == 200
        assert response.context['object_list'] == [
            {"item": item_a, "stock": 0},
            {"item": item_b, "stock": 0}
        ]

    def test_it_returns_by_restaurant(self, client, restaurant_a, item_a):
        response = client.get(f'/ajax/inventory_items?r={restaurant_a.slug}')
        assert response.status_code == 200
        assert response.context['object_list'] == [
            {"item": item_a, "stock": 0}]


@pytest.mark.django_db
class TestInventoryUpdateAjax:
    def test_it_updates_stock(self, client, item_a):
        client.post(
            '/ajax/update_stock',
            {"item_id": item_a.id, "stock": 10}
        )
        recent = Inventory.objects.get(item=item_a)
        assert recent.stock == 10

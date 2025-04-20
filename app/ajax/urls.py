from django.urls import path
from ajax.views import InventoryListlView, UpdateInventoryView

urlpatterns = [
    path(
        'inventory_items',
        InventoryListlView.as_view(),
        name="inventory_items"
    ),
    path(
        "update_stock",
        UpdateInventoryView.as_view(),
        name="update_stock"
    )
]

from django.urls import path
from tracker import views

urlpatterns = [
    path('', views.InventoryPageView.as_view(), name="inventory_page"),
]

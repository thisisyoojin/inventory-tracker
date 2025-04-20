from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse, QueryDict
from django.views.generic.list import ListView
from django.views.generic import View

from tracker.models import Item, Inventory


class InventoryListlView(ListView):
    """
    Ajax view to show a list of inventory
    """
    model = Item
    template = "components/inventory_cards.html"

    def get_items(self, queries: QueryDict):
        kwargs = {}
        if queries.get("r"):
            kwargs["restaurant__slug"] = queries.get("r")
        if queries.get("q_name"):
            kwargs["name__icontains"] = queries.get("q_name")
        return Item.objects.filter(**kwargs)

    def get_queryset(self, queries: QueryDict) -> list:
        items = self.get_items(queries)
        result = []
        for item in items:
            recent_inventory = Inventory.objects.filter(
                item=item).order_by('-created_at').first()
            stock = recent_inventory.stock if recent_inventory else 0
            result.append({"item": item, "stock": stock})
        return result

    def get(self, request: HttpRequest, **kwargs) -> HttpResponse:
        self.object_list = self.get_queryset(request.GET)
        context = self.get_context_data()
        return render(request, self.template, context)


class UpdateInventoryView(View):
    """
    Ajax view to update inventory
    """

    def get(self, request: HttpRequest) -> HttpResponse:
        context = request.GET.dict()
        context["item"] = Item.objects.get(id=context["item_id"])
        return render(request, "components/update_stock.html", context)

    def post(self, request: HttpRequest) -> HttpResponse:
        context = request.POST.dict()
        Inventory.objects.create(
            item=Item.objects.get(id=context["item_id"]),
            stock=context["stock"],
            user=request.user
        )
        return redirect(to="inventory_page")

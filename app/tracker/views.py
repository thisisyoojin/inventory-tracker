from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from django.views.generic import View


def get_html_path(request, template):
    if request.htmx:
        return f"pages/{template}.html"
    return f"pages/{template}_ext.html"


class InventoryPageView(View):
    """
    Showing Inventory Page
    """
    template = "inventory_page"

    def get(self, request: HttpRequest, **kwargs) -> HttpResponse:
        return render(
            request,
            get_html_path(request, self.template),
            {"restaurant": request.GET.get("r")}
        )

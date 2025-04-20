from django.contrib import admin
from tracker.models import Restaurant, Item, Category, Inventory, Order, Supplier

admin.site.register([Restaurant, Category, Item, Inventory, Order, Supplier])

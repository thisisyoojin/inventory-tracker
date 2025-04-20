import uuid
from django.db import models
from django.contrib.auth.models import User


class Item(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, db_index=True)
    restaurant = models.ForeignKey(to="Restaurant", on_delete=models.PROTECT)
    name = models.CharField(max_length=30, unique=True)
    description = models.CharField(max_length=300, null=True, blank=True)
    category = models.ForeignKey(
        to="Category", on_delete=models.SET_NULL, null=True, blank=True
    )
    min_qty = models.SmallIntegerField()
    suppliers = models.ManyToManyField(to="Supplier")
    check_in_Thursday = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"({self.restaurant}) {self.name}: {self.description if self.description else '-'}"


class Category(models.Model):
    name = models.CharField(max_length=30, unique=True)

    def __str__(self):
        return self.name


class Inventory(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, db_index=True)
    item = models.ForeignKey(to="Item", on_delete=models.CASCADE)
    stock = models.SmallIntegerField()
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.item.name}: {self.stock} ({self.created_at.strftime('%Y/%m/%d, %H:%M:%S')})"


class Order(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, db_index=True)
    item = models.ForeignKey(to="Item", on_delete=models.CASCADE)
    item_qty = models.SmallIntegerField()
    item_price = models.FloatField()
    supplier_id = models.ForeignKey(to="Supplier", on_delete=models.DO_NOTHING)
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    created_at = models.DateTimeField(auto_now_add=True)


class Restaurant(models.Model):
    name = models.CharField(max_length=30, unique=True)
    slug = models.CharField(max_length=30, unique=True)

    def __str__(self):
        return self.name


class Supplier(models.Model):
    name = models.CharField(max_length=30, unique=True)
    description = models.CharField(max_length=300, null=True, blank=True)

    def __str__(self):
        return self.name

from django.db import models

from django.shortcuts import reverse
from django.contrib.auth.models import User

from django.conf import settings

# Create your models here.

CATEGORY_CHOICES = (
    ("S", "Shirt"),
    ("SW", "Sportwear"),
    ("OW", "Outwear"),
)

LABEL_CHOICES = (
    ("P", "primary"),
    ("S", "secondary"),
    ("D", "danger"),
)


class Item(models.Model):
    title = models.CharField(max_length=100)
    price = models.FloatField()
    discount_price = models.FloatField(blank=True, null=True)
    category = models.CharField(choices=CATEGORY_CHOICES, max_length=2)
    label = models.CharField(choices=LABEL_CHOICES, max_length=1)
    slug = models.SlugField()
    description = models.TextField(max_length=100000)

    def __str__(self):
        return self.title

    def get_absolute_url(self):  # url for Products
        return reverse("Estore:Product", kwargs={"slug": self.slug})

    def get_add_to_cart_url(self):
        return reverse(
            "Estore:add_to_cart", kwargs={"slug": self.slug}
        )  # url for add_to_cart

    def get_remove_from_cart_url(self):  # url for remove_from_cart
        return reverse("Estore:remove_from_cart", kwargs={"slug": self.slug})


class OrderItem(models.Model):
    ordered = models.BooleanField(default=False)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)  # the quantity of items
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.quantity} of {self.item.title}"


class Order(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    items = models.ManyToManyField(OrderItem)

    ordered = models.BooleanField(default=False)

    start_date = models.DateTimeField(auto_now_add=True)

    ordered_date = models.DateTimeField()

    def __str__(self):
        return self.user.username

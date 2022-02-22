from django.shortcuts import render, get_object_or_404, redirect

from django.views.generic import ListView, DetailView

from Estore.models import Item, Order, OrderItem

from django.utils import timezone

# Create your views here.


class Homeview(ListView):
    model = Item
    template_name = "index.html"


class ItemDetailView(DetailView):
    model = Item
    template_name = "Product.html"


def add_to_cart(request, slug):
    item = get_object_or_404(Item, slug=slug)
    order_item, created = OrderItem.objects.get_or_create(
        item=item, user=request.user, ordered=False
    )
    order_qs = Order.objects.filter(user=request.user, ordered=False)
    if order_qs.exists():
        order = order_qs[0]
        # check if order item is in the order
        if order.items.filter(item__slug=item.slug).exists():
            order_item.quantity += 1
            order_item.save()
        else:
            order.items.add(order_item)
    else:
        ordered_date = timezone.now()
        order = Order.objects.create(user=request.user, ordered_date=ordered_date)
        order.items.add(order_item)

    return redirect("Estore:Product", slug=slug)


# def index(request):

#      context = {

#         'items' : Item.objects.all()
#     }
#      return render(request, 'index.html', context)


def item_list(request):
    context = {"items": Item.objects.all()}
    return render(request, "item_list.html", context)


def Details(request):
    pass
    return render(request, "Details.html")


# def Product(request, pk):
#     pass
#     return render(request, 'Product.html')


# Remove from cart Function


def remove_from_cart(request, slug):
    item = get_object_or_404(Item, slug=slug)
    order_qs = Order.objects.filter(user=request.user, ordered=False)
    if order_qs.exists():
        order = order_qs[0]
        # check if order item is in the order
        if order.items.filter(item__slug=item.slug).exists():
            order_item = OrderItem.objects.filter(
                item=item, user=request.user, ordered=False
            )[0]

            order.items.remove(order_item)
        else:
            return redirect("Estore:Product", slug=slug)

    else:

        return redirect("Estore:Product", slug=slug)

    return redirect("Estore:Product", slug=slug)

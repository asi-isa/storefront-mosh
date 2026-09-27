from django.shortcuts import render
from store.models import Product, OrderItem, Customer, Order
from tags.models import TaggedItem


def hello(request):

    # products = Product.objects.filter(
    #     id__in=OrderItem.objects.values("product_id").distinct()
    # ).order_by("title")

    # last 5 orders with their customers and items
    # orders = (
    #     Order.objects.select_related("customer")
    #     .prefetch_related("orderitem_set__product")
    #     .order_by("-placed_at")[:5]
    # )

    tags = TaggedItem.objects.get_tags_for(Product, 1)

    print(tags)

    return render(request, "playground/hello.html", {"tags": tags})

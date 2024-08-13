from django.db.models import Q
from django.shortcuts import render, get_object_or_404

from burger.models import Burger


def burgers(request):
    all_burgers = Burger.objects.all()
    ctx = {"burgers": all_burgers}
    return render(request, "burger/main_burgers.html", ctx)


def burger_detail(request, pk):
    burger = get_object_or_404(Burger, pk=pk)
    similar_burgers = Burger.objects.filter(
        (
                Q(price__gte=burger.price - 5) & Q(price__lte=burger.price + 5)
        )
    ).exclude(id=burger.id)

    ctx = {"burger": burger, "similar": similar_burgers}
    return render(request, "burger/burger_detail.html", ctx)


def advanced_search(request):
    search_burgers = Burger.objects.all()

    if request.GET:
        name = request.GET.get("name")
        producer = request.GET.get("producer")
        min_price = request.GET.get("min_price")
        max_price = request.GET.get("max_price")
        description = request.GET.get("description")

        search_list = []

        if name:
            search_list.append(Q(title__icontains=name))
        if producer:
            search_list.append(Q(producer=producer))
        if min_price:
            search_list.append(Q(price__gte=min_price))
        if max_price:
            search_list.append(Q(price__lte=max_price))
        if description:
            search_list.append(Q(description__icontains=description))

        for condition in search_list:
            search_burgers &= Burger.objects.filter(condition)

    return render(request, "main_page/advanced_search.html", {"burgers": search_burgers})


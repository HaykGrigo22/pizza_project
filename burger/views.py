from django.core.paginator import Paginator
from django.db.models import Q
from django.shortcuts import render, get_object_or_404

from burger.models import Burger


def main_burgers(request):
    all_burgers = Burger.objects.all()
    paginator = Paginator(all_burgers, 2)

    page_number = request.GET.get("page")
    burgers = paginator.get_page(page_number)
    ctx = {"burgers": burgers}
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

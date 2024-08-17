from django.contrib import messages
from django.core.paginator import Paginator
from django.db.models import Q
from django.shortcuts import render, get_object_or_404, redirect

from burger.forms import AddBurger
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


def add_burger(request):
    if request.method == "POST":
        form = AddBurger(request.POST, request.FILES)
        if form.is_valid():
            try:
                form.save()
                messages.success(request, "Your Burger added successfully!")
                return redirect("burger:burgers")
            except:
                form.add_error(None, "[ERROR] Something went wrong!!!")
    else:
        form = AddBurger()

    return render(request, "burger/add_burger.html", {"form": form})


def delete_burger(request, pk):
    burger = get_object_or_404(Burger, pk=pk)
    if request.method == "POST":
        burger.delete()
        messages.success(request, "The Burger deleted successfully")
        return redirect("burger:burgers")
    return render(request, "burger/delete_burger.html", {"burger": burger})


def update_burger(request, pk):
    burger = get_object_or_404(Burger, pk=pk)
    form = AddBurger(instance=burger)
    if request.method == "POST":
        form = AddBurger(request.POST, request.FILES, instance=burger)
        if form.is_valid():
            form.save()
            messages.success(request, "The Burger updated successfully")
            return redirect("burger:burgers")
    return render(request, "burger/update_burger.html", {"form": form, "burger": burger})

from django.shortcuts import render, get_object_or_404

from main_page.models import Pizzas, Producers


def home(requests):
    all_pizzas = Pizzas.objects.all()
    return render(requests, "main_page/home.html", {"pizzas": all_pizzas})


def pizza_detail(requests, pk):
    pizza = get_object_or_404(Pizzas, pk=pk)
    ctx = {"pizza": pizza}
    return render(requests, "main_page/pizza_detail.html", ctx)


def test(requests):
    all_pizzas = Pizzas.objects.all()
    return render(requests, "main_page/test.html", {"pizzas": all_pizzas})


def about(requests):
    return render(requests, "main_page/about.html")


def producers(requests):
    all_producers = Producers.objects.all()
    return render(requests, "main_page/producers.html", {"producers": all_producers})


def producer_detail(request, pk):
    producer = get_object_or_404(Producers, pk=pk)
    all_pizzas = Pizzas.objects.filter(producer=producer)
    ctx = {"producer": producer, "pizzas": all_pizzas}
    return render(request, "main_page/producer_detail.html", ctx)

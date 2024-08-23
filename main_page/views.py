from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Q
from django.core.paginator import Paginator
from django.forms import inlineformset_factory

from burger.forms import AddBurger
from burger.models import Burger
from main_page.forms import AddPizza, AddProducer, PizzaFormSet, BurgerFormSet
from main_page.models import Pizzas, Producers


def home(request):
    all_pizzas = Pizzas.objects.all()
    paginator = Paginator(all_pizzas, 2)

    page_number = request.GET.get("page")
    pizzas = paginator.get_page(page_number)
    return render(request, "main_page/home.html", {"pizzas": pizzas})


def pizza_detail(request, pk):
    pizza = get_object_or_404(Pizzas, pk=pk)

    similar_pizzas = Pizzas.objects.filter(
        (
            Q(price__gte=pizza.price - 5) & Q(price__lte=pizza.price + 5)
            | Q(thick_type=pizza.thick_type)
        )
    ).exclude(id=pizza.id)

    paginator = Paginator(similar_pizzas, 1)

    page_number = request.GET.get("page")
    sim_pizzas = paginator.get_page(page_number)

    ctx = {"pizza": pizza, "similar": sim_pizzas}
    return render(request, "main_page/pizza_detail.html", ctx)


def about(requests):
    return render(requests, "main_page/about.html")


def producers(request):
    all_producers = Producers.objects.all()
    return render(request, "producer/producers.html", {"producers": all_producers})


def producer_detail(request, pk):
    producer = get_object_or_404(Producers, pk=pk)
    all_pizzas = Pizzas.objects.filter(producer=producer)
    all_burgers = Burger.objects.filter(producer=producer)
    ctx = {"producer": producer, "pizzas": all_pizzas, "burgers": all_burgers}
    return render(request, "producer/producer_detail.html", ctx)


def search(request):
    search_data = request.GET.get("search_data")
    if search_data:
        pizzas = Pizzas.objects.filter(
            Q(title__icontains=search_data) | Q(description__icontains=search_data)
        )
        ctx = {"pizzas": pizzas, "search": search_data}
    else:
        ctx = {"pizzas": Pizzas.objects.all()}

    return render(request, "main_page/search.html", ctx)


def advanced_search(request):
    product_type = request.GET.get('product_type', 'pizza')
    name = request.GET.get("name")
    producer = request.GET.get("producer")
    min_price = request.GET.get("min_price")
    max_price = request.GET.get("max_price")
    description = request.GET.get("description")
    thickness = request.GET.get("thickness") if product_type == 'pizza' else None

    pizzas = Pizzas.objects.all()
    burgers = Burger.objects.all()

    ctx = {}
    search_list = []

    if name:
        search_list.append(Q(title__icontains=name))
    if producer:
        search_list.append(Q(producer__icontains=producer))
    if min_price:
        search_list.append(Q(price__gte=min_price))
    if max_price:
        search_list.append(Q(price__lte=max_price))
    if description:
        search_list.append(Q(description__icontains=description))

    if product_type == 'pizza':
        if thickness:
            search_list.append(Q(thick_type__icontains=thickness))
        for condition in search_list:
            pizzas = pizzas.filter(condition)

        ctx = {"pizzas": pizzas}

    elif product_type == 'burger':
        for condition in search_list:
            burgers = burgers.filter(condition)

        ctx = {"burgers": burgers}

    return render(request, "main_page/advanced_search.html", ctx)


def add_pizza(request):
    if request.method == "POST":
        form = AddPizza(request.POST, request.FILES)
        if form.is_valid():
            try:
                form.save()
                messages.success(request, "Your Pizza added successfully!")
                return redirect("main_page:home")
            except:
                form.add_error(None, "[ERROR] Something went wrong!!!")
    else:
        form = AddPizza()

    return render(request, "main_page/pizza_crud/add_pizza.html", {"form": form})


def delete_pizza(request, pk):
    pizza = get_object_or_404(Pizzas, pk=pk)
    if request.method == "POST":
        pizza.delete()
        messages.success(request, "The Pizza deleted successfully!")
        return redirect("main_page:home")
    return render(request, "main_page/pizza_crud/delete_pizza.html", {"pizza": pizza.title})


def update_pizza(request, pk):
    pizza = get_object_or_404(Pizzas, pk=pk)
    form = AddPizza(instance=pizza)
    if request.method == "POST":
        form = AddPizza(request.POST, request.FILES, instance=pizza)
        if form.is_valid():
            form.save()
            messages.success(request, "The Pizza updated successfully!")
            return redirect("main_page:home")
    return render(request, "main_page/pizza_crud/update_pizza.html", {"form": form, "pizza": pizza})


def add_producer(request):
    if request.method == "POST":
        producer_form = AddProducer(request.POST, request.FILES)
        pizza_formset = PizzaFormSet(request.POST, request.FILES)
        burger_formset = BurgerFormSet(request.POST, request.FILES)

        if producer_form.is_valid() and pizza_formset.is_valid() and burger_formset.is_valid():
            producer = producer_form.save()

            pizzas = pizza_formset.save(commit=False)
            for pizza in pizzas:
                pizza.producer = producer
                pizza.save()

            burgers = burger_formset.save(commit=False)
            for burger in burgers:
                burger.producer = producer
                burger.save()

            messages.success(request, "The Producer created successfully!")
            return redirect("main_page:producers")
    else:
        producer_form = AddProducer()
        pizza_formset = PizzaFormSet()
        burger_formset = BurgerFormSet()

    return render(request, "producer/add_producer.html",
                  {"producer_form": producer_form, "pizza_formset": pizza_formset, "burger_formset": burger_formset})

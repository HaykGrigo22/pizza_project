from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404

from main_page.models import Basket, WishList, Pizzas
from users.forms import LoginForm, RegisterForm
from users.models import Profile


def register(request):
    form = RegisterForm()
    if request.method == "POST":
        form = RegisterForm(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save()
            instance.profile.phone_number = form.cleaned_data["phone_number"]
            instance.profile.image = form.cleaned_data["image"]
            instance.profile.save()
            return redirect("main_page:home")
    return render(request, "user/register.html",
                  {"form": form})


def login_user(request):
    form = LoginForm()
    next_url = request.GET.get("next")

    if request.method == "POST":
        form = LoginForm(request.POST)

        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request, username=cd["username"], password=cd["password"])

            if user:
                login(request, user)
                if next_url:
                    return redirect(next_url)

                return redirect("main_page:home")

    return render(request, "user/login.html", {"form": form})


def logout_user(request):
    logout(request)
    return redirect("main_page:home")


def user_profile(request):
    profile = get_object_or_404(Profile, user=request.user)
    return render(request, "user/profile.html", {"profile": profile})


def user_basket(request):
    if request.user.is_authenticated:
        basket = Basket.objects.filter(user=request.user)
        total_sum = sum(item.product.price * item.quantity for item in basket)
    else:
        basket = request.session.get('basket', {})
        total_sum = 0

        for item in basket.values():
            product = Pizzas.objects.get(pk=item["id"])
            total_sum += product.price * item['quantity']

    return render(request, "user/basket.html", {"baskets": basket, "total_sum": total_sum})


def arrow_up(request, basket_id):
    if request.user.is_authenticated:
        basket = Basket.objects.get(id=basket_id)
        basket.quantity += 1
        basket.save()
    else:
        basket = request.session.get('basket', {})
        basket[str(basket_id)]["quantity"] += 1

        request.session['basket'] = basket
        print(basket)

    return HttpResponseRedirect(request.META.get("HTTP_REFERER"))


def arrow_down(request, basket_id):
    if request.user.is_authenticated:
        basket = Basket.objects.get(id=basket_id)
        if basket.quantity != 1:
            basket.quantity -= 1
            basket.save()
    else:
        basket = request.session.get('basket', {})

        if basket[str(basket_id)]["quantity"] != 1:
            basket[str(basket_id)]["quantity"] -= 1

        request.session['basket'] = basket
        print(basket)

    return HttpResponseRedirect(request.META.get("HTTP_REFERER"))


def basket_delete(request, product_id):
    if request.user.is_authenticated:
        basket = Basket.objects.get(id=product_id)
        basket.delete()
    else:
        basket = request.session.get('basket', {})
        if str(product_id) in basket:
            del basket[str(product_id)]

            request.session['basket'] = basket

    return HttpResponseRedirect(request.META.get("HTTP_REFERER"))


def user_wish_list(request):
    wish_list = WishList.objects.filter(user=request.user)
    return render(request, "user/wish_list.html", {"wish_list": wish_list})


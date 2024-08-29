from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404

from users.forms import LoginForm, RegisterForm
from users.models import Profile


def register(request):
    form = RegisterForm()
    if request.method == "POST":
        form = RegisterForm(request.POST)
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
    name = request.user
    profile = get_object_or_404(Profile, user=name)
    return render(request, "user/profile.html", {"profile": profile})

from django.urls import path
from users import views


app_name = "users"

urlpatterns = [
    path("register/", views.register, name="register"),
    path("login/", views.login_user, name="login"),
    path("log-out/", views.logout_user, name="logout"),
    path("register/", views.register, name="registration"),
    path("my-profile/", views.user_profile, name="user_profile"),
    path("my-basket/", views.user_basket, name="user_basket"),
    path("my-wish-list/", views.user_wish_list, name="wish_list"),
    path("arrow-up/<int:basket_id>", views.arrow_up, name="arrow_up"),
    path("arrow-down/<int:basket_id>", views.arrow_down, name="arrow_down"),
    path("basket-delete/<int:product_id>", views.basket_delete, name="basket_delete"),
]

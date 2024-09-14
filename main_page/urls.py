from django.urls import path
from main_page import views

app_name = "main_page"

urlpatterns = [
    path("", views.home, name="home"),
    path("pizza-info/<int:pk>/", views.pizza_detail, name="pizza_detail"),
    path("about/", views.about, name="about"),
    path("producers/", views.producers, name="producers"),
    path("producer-info/<int:pk>/", views.producer_detail, name="producer_detail"),
    path("search/", views.search, name="search"),
    path("advanced-search/", views.advanced_search, name="advanced_search"),
    path("add-pizza/", views.add_pizza, name="add_pizza"),
    path("delete-pizza/<int:pk>/", views.delete_pizza, name="delete_pizza"),
    path("update-pizza/<int:pk>/", views.update_pizza, name="update_pizza"),
    path("add-producer", views.add_producer, name="add_producer"),
    path("basket-add/<int:product_id>/", views.basket_add, name="basket_add"),
    path("wish-list-add/<int:product_id>/", views.wish_list_add, name="wish_list_add"),
    path("api/all-pizzas")
]

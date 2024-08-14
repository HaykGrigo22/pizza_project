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
    path("advanced_search/", views.advanced_search, name="advanced_search"),
]

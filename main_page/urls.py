from django.urls import path, include
from main_page import views

urlpatterns = [
    path("", views.home, name="home"),
    path("pizza-info/<int:pk>/", views.pizza_detail, name="pizza_detail"),
    path("about/", views.about, name="about"),
    path("producers/", views.producers, name="producers"),
    path("producer-info/<int:pk>/", views.producer_detail, name="producer_detail"),
]

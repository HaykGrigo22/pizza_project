from django.urls import path
from burger import views


app_name = "burger"

urlpatterns = [
    path("burgers/", views.main_burgers, name="burgers"),
    path("burger-info/<int:pk>/", views.burger_detail, name="burger_detail"),
    path("add-burger/", views.add_burger, name="add_burger"),
    path("delete-burger/<int:pk>/", views.delete_burger, name="delete_burger"),
    path("update-burger/<int:pk>", views.update_burger, name="update_burger"),
]

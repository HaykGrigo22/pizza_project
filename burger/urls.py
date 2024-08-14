from django.urls import path
from burger import views


app_name = "burger"

urlpatterns = [
    path("burgers/", views.main_burgers, name="burgers"),
    path("burger-info/<int:pk>/", views.burger_detail, name="burger_detail"),
]

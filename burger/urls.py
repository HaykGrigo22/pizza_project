from django.urls import path
from burger import views


app_name = "burger"

urlpatterns = [
    path("burgers/", views.burgers, name="burgers"),
    path("burger-info/<int:pk>/", views.burger_detail, name="burger_detail"),
    path("advanced_search/", views.advanced_search, name="advanced_search"),
]

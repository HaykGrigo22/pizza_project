from django.urls import path
from users import views


app_name = "users"

urlpatterns = [
    path("register/", views.register, name="register"),
    path("login/", views.login_user, name="login"),
    path("log-out/", views.logout_user, name="logout"),
    path("register/", views.register, name="registration"),
    path("my-profile/", views.user_profile, name="user_profile"),
]

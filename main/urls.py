from django.urls import path
import views

urlpatterns = [
    path("login/", views.Login.as_view(), name="Login"),
    path("home/", views.Home.as_view(), name="Home"),
    path("creatUser/", views.CreateUser.as_view(), name="create user"),
    path("searchApi/", views.Search.as_view(), name="search"),

]
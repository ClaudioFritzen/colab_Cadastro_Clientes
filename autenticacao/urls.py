from django.urls import path, include
from . import views



urlpatterns = [
    path('cadastro/', views.home, name="cadastro" ),
    path('', views.home, name="home"),
    path('login/', views.login, name="login"),

]

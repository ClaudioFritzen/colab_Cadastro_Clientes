from django.urls import path, include
from . import views



urlpatterns = [
    path('', views.home, name="cadastro" ),
    path('login/', views.login, name="login"),

]

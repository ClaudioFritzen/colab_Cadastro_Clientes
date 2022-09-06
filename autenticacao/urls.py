from django.urls import path, include
from . import views



urlpatterns = [
    path('', views.cadastro, name="cadastro" ),
    path('login/', views.login, name="login"),

]

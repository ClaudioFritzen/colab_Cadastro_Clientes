from django.urls import path, include
from . import views

# urls de redirecionamento
urlpatterns = [
    path('', views.cadastro, name="cadastro" ),
    path('login/', views.login, name="login"),
    path('sair/', views.sair, name="sair"), 
]

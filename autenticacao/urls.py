from django.urls import path, include
from . import views

# import para fazer alteração da senha
from django.contrib.auth import views as auth_views


# urls de redirecionamento
urlpatterns = [
    path('', views.cadastro, name="cadastro" ),
    path('login/', views.login, name="login"),
    path('sair/', views.sair, name="sair"),
    path('recuperar_senha/', views.recuperar_senha, name="recuperar_senha"),
    path('pagefinal/', views.pagefinal, name="pagefinal"),
    
    # reset password urls
    path('password_reset/', auth_views.PasswordResetView.as_view(),name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
]

from django.urls import path
from . import views


app_name = 'users'  # Пространство имен для приложения

urlpatterns = [
    path('login/', views.LoginUser.as_view(), name='login'),
    path('logout/', views.LogoutUser.as_view(), name='logout'),
    path('signup/', views.RegisterUser.as_view(), name='signup'),
    path('register_done/', views.RegisterDone.as_view(), name='register_done'),
    path('profile/', views.ProfileUser.as_view(), name='profile'),  # Маршрут к профилю пользователя
    path('profile_cards/', views.UserCardsView.as_view(), name='profile_cards'),
    path('password_change/', views.UserPasswordChange.as_view(), name='password_change'),
    path('password_change/done/', views.UserPasswordChangeDone.as_view(), name='password_change_done'),

    ]

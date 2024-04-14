from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.views import LoginView, LogoutView
from .forms import LoginUserForm
from django.urls import reverse, reverse_lazy



class LoginUser(LoginView):
    form_class = LoginUserForm
    template_name = 'users/login.html'
    extra_context = {'title': 'Авторизация'}

    def get_success_url(self):
        return reverse_lazy('index')
    

class LogoutUser(LogoutView):
    next_page = reverse_lazy('users:login')




def signup_user(request):
    pass
from re import T
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.views import LoginView, LogoutView
from .forms import LoginUserForm, RegisterUserForm
from django.urls import reverse, reverse_lazy
from django.views.generic import TemplateView


class RegisterDone(TemplateView):
    template_name = 'users/register_done.html'
    extra_context = {'title': 'Регистрация завершена'}


class LoginUser(LoginView):
    form_class = LoginUserForm
    template_name = 'users/login.html'
    extra_context = {'title': 'Авторизация'}

    def get_success_url(self):
        return reverse_lazy('index')
    

class LogoutUser(LogoutView):
    next_page = reverse_lazy('users:login')



def signup_user(request):
    if request.method == 'POST':
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])  # Устанавливаем пароль
            user.save()
            return redirect('users:register_done')  # Перенаправляем на страницу успешной регистрации
    else:
        form = RegisterUserForm()  # Пустая форма для GET-запроса
    return render(request, 'users/register.html', {'form': form})
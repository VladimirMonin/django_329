# myapp/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('catalog/', views.catalog, name='catalog'),
    # Другие URL-паттерны для приложения
]
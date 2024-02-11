# myapp/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('catalog/', views.catalog, name='catalog'),
    # Карточки по ID
    path('catalog/<int:card_id>/', views.get_card_by_id, name='card'),
    # Другие URL-паттерны для приложения
]
"""
anki/urls.py
"""
from django.contrib import admin
from django.urls import path, include
import debug_toolbar
from django.conf import settings

from cards import views

urlpatterns = [
    # Админка
    path('admin/', admin.site.urls),
    # Маршруты для меню
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    # Маршруты подключенные из приложения cards
    path('cards/', include('cards.urls')),

]

if settings.DEBUG:
    urlpatterns = [
                      path('__debug__/', include(debug_toolbar.urls)),
                      # другие URL-паттерны
                  ] + urlpatterns

"""
python manage.py createsuperuser - создание суперпользователя
"""

from django.contrib import admin

from .models import Card


@admin.register(Card)
class CardAdmin(admin.ModelAdmin):
    pass

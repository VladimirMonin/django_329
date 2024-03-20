"""
python manage.py createsuperuser - создание суперпользователя
"""

from django.contrib import admin

from .models import Card, Category, Tag, CardTags


@admin.register(Card)
class CardAdmin(admin.ModelAdmin):
    pass


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    pass


@admin.register(CardTags)
class CardTagsAdmin(admin.ModelAdmin):
    pass

# Откатить все миграции python manage.py migrate zero
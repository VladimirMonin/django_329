"""
python manage.py createsuperuser - создание суперпользователя
"""

from django.contrib import admin

from .models import Card, Category, Tag, CardTags



@admin.register(Card)
class CardAdmin(admin.ModelAdmin):
    """
    Класс для отображения модели Card в админке Django
    Имеет поле поиска по тегу, а так же поиск по вопросу и ответу
    """
    search_fields = ['tags__name']


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
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

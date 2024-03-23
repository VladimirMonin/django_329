"""
python manage.py createsuperuser - создание суперпользователя
Есть 2 варианта регистрации
admin.site.register() или @admin.register()
"""

from django.contrib import admin

from .models import Card, Category, Tag, CardTags


@admin.register(Card)
class CardAdmin(admin.ModelAdmin):
    list_display = ('get_questions', 'upload_date', 'category_name', 'tags_list')

    # Добавляем метод для отображения названия категории
    def category_name(self, obj):
        return obj.category_id.name
    category_name.short_description = 'Категория'  # Название колонки в админке

    # Дополнительный метод для отображения списка тегов
    def tags_list(self, obj):
        return " | ".join([tag.name for tag in obj.tags.all()])
    tags_list.short_description = 'Теги'


    # Дополнительный метод для отображения вопросов
    def get_questions(self, obj):
        row_question = obj.question
        result_question = row_question.replace('##', '').replace('`', '').replace('**', '').replace('*', '')
        return result_question
    get_questions.short_description = 'Вопрос'

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    pass


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass


@admin.register(CardTags)
class CardTagsAdmin(admin.ModelAdmin):
    # Отображаемые поля
    list_display = ('card', 'tag')

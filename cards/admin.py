"""
python manage.py createsuperuser - создание суперпользователя
Есть 2 варианта регистрации
admin.site.register() или @admin.register()
@admin.display() - декоратор для отображения дополнительных полей
параметры декоратора: description - название поля, ordering - сортировка (реальное поле из модели)
"""

from django.contrib import admin

from .models import Card, Category, Tag, CardTags


@admin.register(Card)
class CardAdmin(admin.ModelAdmin):
    list_display = ('get_questions', 'upload_date', 'category_name', 'tags_list', 'brief_info')
    list_display_links = ('get_questions',)
    list_filter = ('category_id', 'check_status')
    search_fields = ('question', 'category_id__name', 'answer', 'tags__name')
    ordering = ('-upload_date', 'question')
    list_per_page = 20

    # list_editable = ('category_name',) # Редактируемое поле
    # Добавляем метод для отображения названия категории
    @admin.display(description="Категория", ordering='category_id__name')
    def category_name(self, obj):
        return obj.category_id.name

    # Дополнительный метод для отображения списка тегов
    @admin.display(description="Теги", ordering='tags__name')
    def tags_list(self, obj):
        return " | ".join([tag.name for tag in obj.tags.all()])

    # Определение метода для отображения краткой информации о карточке
    # ordering по полю answer, так как точного поля для сортировки по краткому описанию нет
    @admin.display(description="Краткое описание", ordering='answer')
    def brief_info(self, card):
        # Определяем длину ответа
        length = len(card.answer)
        # Проверяем наличие кода
        has_code = 'Да' if '```' in card.answer else 'Нет'
        return f"Длина ответа: {length}, Код: {has_code}"

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

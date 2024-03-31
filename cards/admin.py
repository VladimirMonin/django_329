"""
python manage.py createsuperuser - создание суперпользователя
Есть 2 варианта регистрации
admin.site.register() или @admin.register()
@admin.display() - декоратор для отображения дополнительных полей
параметры декоратора: description - название поля, ordering - сортировка (реальное поле из модели)
"""

from django.contrib import admin

from .models import Card, Category, Tag, CardTags


class CheckStatusFilter(admin.SimpleListFilter):
    title = 'Статус проверки' # Название фильтра, которое будет отображаться в админке
    parameter_name = 'check_status' # Имя параметра, который будет передаваться в URL

    def lookups(self, request, model_admin):
        """
        Метод для определения значений фильтрации
        Возвращает кортежи с двумя значениями: значение и отображаемое имя
        :param request:
        :param model_admin:
        :return:
        """
        return (
            ('UNCHECKED', 'Не проверено'),
            ('CHECKED', 'Проверено'),
        )

    def queryset(self, request, queryset):
        """
        Метод для фильтрации
        self.value() - получение значения фильтра
        :param request:
        :param queryset:
        :return:
        """
        if self.value() == 'UNCHECKED':
            return queryset.filter(check_status=0)
        if self.value() == 'CHECKED':
            return queryset.filter(check_status=1)


@admin.register(Card)
class CardAdmin(admin.ModelAdmin):
    list_display = ('get_questions', 'check_status', 'upload_date', 'category_name', 'tags_list', 'brief_info')
    list_editable = ('check_status',)
    list_display_links = ('get_questions',)
    list_filter = ('category_id', CheckStatusFilter)
    search_fields = ('question', 'category_id__name', 'answer', 'tags__name')
    ordering = ('-upload_date', 'question')
    list_per_page = 20
    actions = ['mark_as_checked', 'mark_as_unchecked']
    fields = ('question', 'answer', 'category_id') #TODO tags - ошибка из за "through" - надо переделывать модель многие ко многим
    # filter_horizontal = ('tags',)

    # list_editable = ('category_name',) # Редактируемое поле
    # Добавляем метод для отображения названия категории
    @admin.display(description="Категория", ordering='category_id__name')
    def category_name(self, obj):
        return obj.category_id.name if obj.category_id else 'Без категории'

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

    @admin.action(description='Отметить как проверенные')
    def mark_as_checked(self, request, queryset):
        queryset.update(check_status=1)


    @admin.action(description='Отметить как непроверенные')
    def mark_as_unchecked(self, request, queryset):
        queryset.update(check_status=0)


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

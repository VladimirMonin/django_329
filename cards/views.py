"""
cards/views.py
index - возвращает главную страницу - шаблон /templates/cards/main.html
about - возвращает страницу "О проекте" - шаблон /templates/cards/about.html
catalog - возвращает страницу "Каталог" - шаблон /templates/cards/catalog.html


get_categories - возвращает все категории для представления в каталоге
get_cards_by_category - возвращает карточки по категории для представления в каталоге
get_cards_by_tag - возвращает карточки по тегу для представления в каталоге
get_detail_card_by_id - возвращает детальную информацию по карточке для представления

render(запрос, шаблон, контекст=None)
    Возвращает объект HttpResponse с отрендеренным шаблоном шаблон и контекстом контекст.
    Если контекст не передан, используется пустой словарь.
"""
from django.db.models import F, Q
from django.http import HttpResponse, JsonResponse
from .models import Card
from django.shortcuts import get_object_or_404, redirect
from django.views.decorators.cache import cache_page
from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import CardModelForm
from django.core.paginator import Paginator
from django.template.loader import render_to_string
from django.views import View
from django.views.generic import TemplateView
from django.views.generic.list import ListView
info = {

    "menu": [
        {"title": "Главная",
         "url": "/",
         "url_name": "index"},
        {"title": "О проекте",
         "url": "/about/",
         "url_name": "about"},
        {"title": "Каталог",
         "url": "/cards/catalog/",
         "url_name": "catalog"},
    ],
}


class IndexView(TemplateView):
    template_name = 'main.html'  # Указываем имя шаблона для отображения
    # Предполагаем, что info - это словарь с данными, который мы хотим передать в шаблон
    extra_context = info

class AboutView(TemplateView):
    template_name = 'about.html'  # Аналогично указываем имя шаблона
    extra_context = info






# @cache_page(60 * 15)  # Кэширует на 15 минут
def catalog(request):
    """
    Функция для отображения каталога карточек с возможностью сортировки.
    Параметры GET запроса:
    - sort: ключ для сортировки (допустимые значения: 'upload_date', 'views', 'adds').
    - order: порядок сортировки ('asc' для возрастания, 'desc' для убывания; по умолчанию 'desc').
    """
    # Считываем параметры из GET запроса
    sort = request.GET.get('sort', 'upload_date')  # по умолчанию сортируем по дате загрузки
    order = request.GET.get('order', 'desc')  # по умолчанию используем убывающий порядок
    search_query = request.GET.get('search_query', '')  # поиск по вопросу
    page_number = request.GET.get('page', 1)  # Номер страницы
    # Сопоставляем параметр сортировки с полями модели
    valid_sort_fields = {'upload_date', 'views',
                         'favorites'}  # Исправил 'adds' на 'favorites', предполагая, что это опечатка
    if sort not in valid_sort_fields:
        sort = 'upload_date'  # Возвращаемся к сортировке по умолчанию, если передан неверный ключ сортировки

    # Обрабатываем порядок сортировки
    if order == 'asc':
        order_by = sort
    else:
        order_by = f'-{sort}'

    if not search_query:
        # Получаем отсортированные карточки через ЖАДНУЮ ЗАГРУЗКУ
        cards = Card.objects.prefetch_related('tags').order_by(order_by)

    else:
        # Фильтруем карточки по вопросу
        # cards = Card.objects.filter(question__icontains=search_query).prefetch_related('tags').order_by(order_by)

        # Жадная загрузка с использованием фильтра и Q-объектов (содержание в вопросе или ответе)
        # cards = Card.objects.prefetch_related('tags').filter(Q(question__icontains=search_query) | Q(answer__icontains=search_query)).order_by(order_by)

        # Жадная загрузка с использованием фильтра и Q-объектов (содержание в вопросе или совпадение с тегом) уникальные объекты
        cards = Card.objects.prefetch_related('tags').filter(Q(question__icontains=search_query) | Q(tags__name__icontains=search_query) | Q(answer__icontains=search_query)).order_by(order_by).distinct()

    # Создаем объект пагинатора
    paginator = Paginator(cards, 30)
    page_obj = paginator.get_page(page_number)
    context = {
        'cards': page_obj,  # Передаем объект страницы в контекст
        'sort': sort,  # Добавлено для возможности отображения текущей сортировки в шаблоне
        'order': order,  # Добавлено для возможности отображения текущего порядка в шаблоне
        'menu': info['menu'],  # Добавлено для отображения меню на странице
        'page_obj': page_obj,  # Добавлено для передачи объекта страницы в шаблон
    }
    return render(request, 'cards/catalog.html', context)


class CatalogView(ListView):
    model = Card  # Указываем модель, данные которой мы хотим отобразить
    template_name = 'cards/catalog.html'  # Путь к шаблону, который будет использоваться для отображения страницы
    context_object_name = 'cards'  # Имя переменной контекста, которую будем использовать в шаблоне
    paginate_by = 30  # Количество объектов на странице

    # Метод для модификации начального запроса к БД
    def get_queryset(self):
        # Получение параметров сортировки из GET-запроса
        sort = self.request.GET.get('sort', 'upload_date')
        order = self.request.GET.get('order', 'desc')
        search_query = self.request.GET.get('search_query', '')

        # Определение направления сортировки
        if order == 'asc':
            order_by = sort
        else:
            order_by = f'-{sort}'

        # Фильтрация карточек по поисковому запросу и сортировка
        if search_query:
            queryset = Card.objects.filter(
                Q(question__icontains=search_query) |
                Q(answer__icontains=search_query) |
                Q(tags__name__icontains=search_query)
            ).distinct().order_by(order_by)
        else:
            queryset = Card.objects.all().order_by(order_by)
        return queryset

    # Метод для добавления дополнительного контекста
    def get_context_data(self, **kwargs):
        # Получение существующего контекста из базового класса
        context = super().get_context_data(**kwargs)
        # Добавление дополнительных данных в контекст
        context['sort'] = self.request.GET.get('sort', 'upload_date')
        context['order'] = self.request.GET.get('order', 'desc')
        context['search_query'] = self.request.GET.get('search_query', '')
        # Добавление статических данных в контекст, если это необходимо
        context['menu'] = info['menu'] # Пример добавления статических данных в контекст
        return context



def get_categories(request):
    """
    Возвращает все категории для представления в каталоге
    """
    # Проверка работы базового шаблона
    return render(request, 'base.html', info)


def get_cards_by_category(request, slug):
    """
    Возвращает карточки по категории для представления в каталоге
    """
    return HttpResponse(f'Cards by category {slug}')


@cache_page(60 * 15)  # Кэширует на 15 минут
def get_cards_by_tag(request, tag_id):
    """
    Возвращает карточки по тегу для представления в каталоге
    Мы используем многие-ко-многим, получая все карточки, которые связаны с тегом
    Временно, мы будем использовать шаблон каталога
    """
    # cards = Card.objects.filter(tags=tag_id)

    # Жадная загрузка
    cards = Card.objects.filter(tags=tag_id).prefetch_related('tags')
    context = {
        'cards': cards,
        'cards_count': cards.count(),
        'menu': info['menu'],
    }
    return render(request, 'cards/catalog.html', context)


def get_detail_card_by_id(request, card_id):
    card_obj = get_object_or_404(Card.objects.prefetch_related('tags'), pk=card_id)

    # Обновление счетчика просмотров
    Card.objects.filter(pk=card_id).update(views=F('views') + 1)

    card = {
        "card": card_obj,
        "menu": info["menu"],
    }

    return render(request, 'cards/card_detail.html', card, status=200)


class AddCardView(View):
    # Метод для обработки GET-запросов
    def get(self, request, *args, **kwargs):
        form = CardModelForm()  # Создаем пустую форму
        context = {
            'form': form,
            # предполагаем, что info['menu'] - это данные, необходимые для отображения меню на странице
            'menu': info['menu'],  
        }
        return render(request, 'cards/add_card.html', context)
    
    # Метод для обработки POST-запросов
    def post(self, request, *args, **kwargs):
        form = CardModelForm(request.POST)
        if form.is_valid():
            card = form.save()  # Сохраняем форму, если она валидна
            # Перенаправляем пользователя на страницу созданной карточки
            return redirect(card.get_absolute_url())
        else:
            # Если форма не валидна, возвращаем ее обратно в шаблон с ошибками
            context = {
                'form': form,
                'menu': info['menu'],
            }
            return render(request, 'cards/add_card.html', context)



def preview_card_ajax(request):
    if request.method == "POST":
        question = request.POST.get('question', '')
        answer = request.POST.get('answer', '')
        category = request.POST.get('category', '')

        # Генерация HTML для предварительного просмотра
        html_content = render_to_string('cards/card_detail.html', {
            'card': {
                'question': question,
                'answer': answer,
                'category': 'Тестовая категория',
                'tags': ['тест', 'тег'],

            }
        }
                                        )

        return JsonResponse({'html': html_content})
    # return JsonResponse({'error': 'Invalid request'}, status=400)
    return HttpResponseRedirect('/cards/add/')
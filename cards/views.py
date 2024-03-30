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
from django.db.models import F
from django.http import HttpResponse
from .models import Card
from django.shortcuts import get_object_or_404
from django.views.decorators.cache import cache_page
from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import CardForm

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


def index(request):
    """Функция для отображения главной страницы
    будет возвращать рендер шаблона root/templates/main.html"""
    return render(request, "main.html", info)


def about(request):
    """Функция для отображения страницы "О проекте"
    будет возвращать рендер шаблона /root/templates/about.html"""
    return render(request, 'about.html', info)


@cache_page(60 * 15)  # Кэширует на 15 минут
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

    # Получаем отсортированные карточки через ЖАДНУЮ ЗАГРУЗКУ
    cards = Card.objects.prefetch_related('tags').order_by(order_by)

    context = {
        'cards': cards,
        'cards_count': len(cards),
        'sort': sort,  # Добавлено для возможности отображения текущей сортировки в шаблоне
        'order': order,  # Добавлено для возможности отображения текущего порядка в шаблоне
        'menu': info['menu'],  # Добавлено для отображения меню на странице
    }
    return render(request, 'cards/catalog.html', context)


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


def add_card(request):
    if request.method == 'POST':
        form = CardForm(request.POST)
        if form.is_valid():
            # Извлекаем данные для сохранения
            card_answer = form.cleaned_data['answer']
            card_question = form.cleaned_data['question']
            card_category = form.cleaned_data['category']

            # Проверяем, существует ли карточка с таким вопросом, или с таким ответом
            # Используем метод exists() для проверки наличия объектов в базе данных
            if Card.objects.filter(question=card_question).exists() or Card.objects.filter(answer=card_answer).exists():
                form.add_error('question', 'Карточка не может быть добавлена, так как уже существует карточка с таким вопросом или ответом')
                context = {
                    'form': form,
                    'menu': info['menu'],
                }
                return render(request, 'cards/add_card.html', context, status=400)


            # Создаем новую карточку
            card = Card.objects.create(
                question=card_question,
                answer=card_answer,
                category_id=card_category
            )

            # Получаем ID созданной карточки
            card_id = card.card_id

            # Сохраняем карточку
            card.save()

            # status 200 todo - изменить на 201, происходит редирект на самого себя?!
            return HttpResponseRedirect(f'/cards/{card_id}/detail/')

        else:
            # Если форма не валидна, вернем страницу с формой и ошибками
            context = {
                'form': form,
                'menu': info['menu'],
            }
            return render(request, 'cards/add_card.html', context, status=400)
    else:
        form = CardForm()
        context = {
            'form': form,
            'menu': info['menu'],
        }

    return render(request, 'cards/add_card.html', context, status=200)

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

from django.http import HttpResponse
from django.shortcuts import render
from .models import Card
from django.shortcuts import get_object_or_404


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


def catalog(request):
    """
    /cards/catalog/
    Функция для отображения страницы "Каталог"
    будет возвращать рендер шаблона /templates/cards/catalog.html"""
    return render(request, 'cards/catalog.html', info)


from django.http import HttpResponse


def catalog2(request):
    """
    /cards/catalog2/
    Экспериментальный каталог под GET запросы.
    Отдаём в ответе все параметры GET запроса или сообщение об отсутствии ожидаемых параметров.
    :param request:
    :return: HttpResponse
    """
    # Получаем значения параметров 'OrderBy' и 'Limit' из GET запроса
    order_by = request.GET.get('OrderBy')
    limit = request.GET.get('Limit')

    # Строим ответ в зависимости от переданных параметров
    response_text = []

    if order_by:
        response_text.append(f'Сортировка по {order_by}')
    if limit:
        response_text.append(f'Лимит: {limit}')

    # Если были переданы ожидаемые параметры, объединяем их в одну строку и возвращаем
    if response_text:
        return HttpResponse('<br>'.join(response_text))

    # Если ожидаемые параметры не были переданы, возвращаем сообщение об ошибке
    return HttpResponse('Ожидаемые параметры не переданы. Необходимо передать параметры для '
                        'сортировки (OrderBy) или лимита (Limit).', status=404)


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


def get_cards_by_tag(request, slug):
    """
    Возвращает карточки по тегу для представления в каталоге
    """
    return HttpResponse(f'Cards by tag {slug}')


def get_detail_card_by_id(request, card_id):
    """
    /cards/<int:card_id>/detail/
    Возвращает шаблон cards/templates/cards/card_detail.html с детальной информацией по карточке
    """

    # Добываем карточку из БД через get_object_or_404
    # если карточки с таким id нет, то вернется 404
    card = {
        "card": get_object_or_404(Card, id=card_id),
        "menu": info["menu"]
    }

    return render(request, 'cards/card_detail.html', card, status=200)

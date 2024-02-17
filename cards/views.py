"""
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
from django.template.context_processors import request


def index(request):
    """Функция для отображения главной страницы
    будет возвращать рендер шаблона /templates/cards/main.html"""
    return render(request, 'cards/main.html')


def about(request):
    """Функция для отображения страницы "О проекте"
    будет возвращать рендер шаблона /templates/cards/about.html"""
    return render(request, 'cards/about.html')


def catalog(request):
    """Функция для отображения страницы "Каталог"
    будет возвращать рендер шаблона /templates/cards/catalog.html"""
    return render(request, 'cards/catalog.html')



def get_categories(request):
    """
    Возвращает все категории для представления в каталоге
    """
    return HttpResponse('All categories')


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
    Возвращает детальную информацию по карточке для представления
    """
    return HttpResponse(f'Detail card by id {card_id}')

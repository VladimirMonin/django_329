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
from linecache import cache
from django.db.models import F, Q, Prefetch
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
from django.views.generic.detail import DetailView
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


        queryset = Card.objects.prefetch_related('tags').all()

        # Фильтрация карточек по поисковому запросу и сортировка
        # select_related - для оптимизации запроса, чтобы избежать дополнительных запросов к БД
        if search_query:
            queryset = queryset.filter(
                Q(question__icontains=search_query) |
                Q(answer__icontains=search_query) |
                Q(tags__name__icontains=search_query)
            ).distinct().order_by(order_by)
        else:
            queryset = queryset.order_by(order_by)

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


class CardDetailView(DetailView):
    model = Card
    template_name = 'cards/card_detail.html'
    context_object_name = 'card'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = info['menu']
        return context





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
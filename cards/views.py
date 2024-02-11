from django.http import HttpResponse

def index(request):
    return HttpResponse("Привет, мир!")

def catalog(request):
    return HttpResponse("Каталог карточек")


def get_card_by_id(request, card_id):
    return HttpResponse(f"Карточка {card_id}")


def get_category_by_name(request, slug):
    return HttpResponse(f"Категория {slug}")
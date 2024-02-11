from django.http import HttpResponse

def index(request):
    return HttpResponse("Привет, мир!")

def catalog(request):
    return HttpResponse("Каталог карточек")
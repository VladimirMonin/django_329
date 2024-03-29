# django_329
Учебный проект Django с группой python329

## Lesson 54

- Создан репозиторий django_329
- Создано виртуальное окружение `python -m venv venv`
- Активировано виртуальное окружение `venv\Scripts\activate`
- Установлен Django 4.2
- Создан проект anki `django-admin startproject anki .` (точка в конце команды создает проект в текущей директории)
- Создана ветка `develop` и переключен на нее
- Создан приложение `cards` команда `python manage.py startapp cards`
- Подключен `cards` в `settings.py`
- Создано первое представление `index` в `views.py` в приложении `cards`
- Создан url для `index` в  `aniki` в `urls.py`
- Получили свой первый `HttpResponse` в браузере "Hello, World!"
- Для того чтобы убрать ошибки импорта в `urls.py` ищем в какой папке `manage.py` и Отмечаем ее как `source root` в PyCharm
- В приложении `cards` создан файл `urls.py` и подключен в `aniki` в `urls.py` через функцию `include`
- Протестирован маршрут `cards/catalog/` и получен ответ Каталог карточек
- Созданы маршрут `cards.urls` и представление `cards/catalog/<int:card_id>/` которое позволяет делать GET запросы к карточке по id
- Созданы маршрут в `cards.urls` и  `catalog/<slug:slug>/` и представление `get_category_by_name` которое позволяет делать GET запросы к карточке по slug
- Созданы тесты для представлений `cards` в `tests.py` в приложении `cards` (для запуска тестов используем команду `python manage.py test cards`)


## Lesson 55
Решено остановиться на следующей версии маршрутов:

### Главная страница и меню
1. **Главная страница**: `/` - главная страница сайта с общей информацией и ссылками на различные разделы.
2. **О проекте**: `/about/` - страница с информацией о проекте, его целях и создателях.


### Пользователи `/users/`

1. **Регистрация пользователя**: `/users/register/` - страница для регистрации новых пользователей.
2. **Авторизация пользователя**: `/users/login/` - страница для входа в систему существующих пользователей через email и пароль или через ВКонтакте.
3. **Восстановление доступа (сброс пароля)**: `/users/password_reset/` - начало процесса восстановления доступа, включая ввод email для отправки инструкций по сбросу пароля.
4. **Смена пароля**: `/users/password_change/` - страница для смены пароля авторизованным пользователями.
5. **Личный кабинет пользователя**: `/users/profile/<user_id>/` - страница личного кабинета пользователя, где он может повторять карточки и настраивать свой профиль.
6. **Просмотр профиля другого пользователя**: `/users/profile/<user_id>/view` - страница для просмотра профилей других пользователей с информацией о добавленных карточках и основных данных пользователя.

### Карточки `/cards/`
1. **Каталог карточек**: `/cards/catalog/` - страница со списком всех карточек.
2. **Категории карточек**: `/cards/categories/` - страница со списком категорий карточек.
3. **Карточки по категории**: `/cards/categories/<category_slug>/` - отображение карточек определенной категории.
4. **Теги карточек**: `/cards/tags/<tag_slug>/` - отображение карточек, отмеченных определенным тегом.
5. **Детальная информация по карточке**: `/cards/<kart_id>/detail/` - страница с подробной информацией о карточке, включая комментарии и возможность добавления в избранное.

### Разделение

Разделение URL для личного кабинета пользователя и просмотра профилей других пользователей не обязательно, и выбор структуры URL зависит от конкретных требований и предпочтений разработки вашего приложения. Однако, есть несколько соображений, которые могут помочь вам принять решение:

### Единый URL для Профилей
Использование единого URL для обоих действий, например, `/users/profile/<user_id>/`, может упростить структуру URL и сделать систему маршрутизации менее запутанной. В этом случае, логика определения, показывать ли интерфейс редактирования профиля или только страницу просмотра, может быть реализована на уровне контроллера или представления в зависимости от того, соответствует ли `user_id` текущему авторизованному пользователю.

**Преимущества**:
- Упрощенная структура URL.
- Меньше дублирования в маршрутизации и шаблонах.

**Недостатки**:
- Необходима дополнительная логика в представлениях для разграничения доступа и функционала.

### Раздельные URL для Разных Действий
Предоставление разных URL для просмотра и редактирования профиля, как вы предложили (`/users/profile/<user_id>/` для личного кабинета и `/users/profile/<user_id>/view` для просмотра других профилей), может облегчить разграничение доступа и ясно отделять функционал между разными видами пользовательских взаимодействий.

**Преимущества**:
- Четкое разделение функционала и доступа.
- Более очевидная структура URL для разработчиков и возможно для пользователей.

**Недостатки**:
- Необходимость поддерживать более сложную структуру маршрутизации.
- Возможное дублирование кода для похожих представлений и шаблонов.

### Рекомендация
Решение о структуре URL должно базироваться на вашей целевой аудитории, общей архитектуре приложения и предпочтениях в удобстве разработки и поддержке. Если ваше приложение стремится к максимальной прозрачности и простоте для пользователя, единый URL может быть лучшим выбором. Однако, если для вас важнее четкое разделение функционала и управления доступом, раздельные URL могут обеспечить более строгую организацию.

В любом случае, важно тщательно продумать систему прав и доступов, чтобы избежать утечки личной информации и несанкционированного доступа к функциям редактирования профиля.

## Lesson 56
- Изучали шаблоны
- Был сделан базовый шаблон
- Передача данных в шаблон через контекст
- Было рассмотрено наследование шаблонов через `{% block %}` и `include`
- Доступность переменных в наследуемых шаблонах
- Подключение статических файлов
- Шаблонный тег для подключения статических файлов `{% load static %}` и использование `{% static 'path' %}`

## Домашнее задание к уроку 56: №36

Разработать структуру шаблонов для Django-приложения, включая базовый шаблон и наследуемые от него шаблоны для главной 
страницы, страницы "О проекте", каталога карточек и детального представления карточки. 
Необходимо обеспечить подключение статики, создание кликабельного меню и отображение карточек.

### Шаблоны
`root/templates/base.html`
`root/templates/main.html`
`root/templates/about.html`
`cards/templates/cards/catalog.html`
`cards/templates/cards/card_detail.html`
`cards/templates/cards/card_detail.html`
`root/templates/include/menu.html`

```python
# Пример данных для карточек  
cards_dataset = [  
    {        "question": "Что такое PEP 8?",  
        "answer": "PEP 8 — стандарт написания кода на Python.",  
        "category": "Стандарты кода",  
        "tags": ["PEP 8", "стиль", "форматирование"],  
        "id_author": 1,
        "id_card": 1,  
        "upload_date": "2023-01-15",  
        "views_count": 100,  
        "favorites_count": 25  
    },
```
## Lesson 57:
02.03.2024
- Разбор домашнего задания
- Создание пользователького тега шаблонов
- Знакомство с Django ORM
- Создание первой модели `Card` и миграция

## Lesson 58:
03.03.2024
- Работа с миграциями
- Команда `python manage.py makemigrations` создает файл миграции
- Команда `python manage.py migrate` применяет миграции
- Команда `python manage.py sqlmigrate cards 0001` показывает SQL код миграции
- Команда `python manage.py showmigrations` показывает статус миграций
- Команда `python manage.py migrate cards zero` откатывает все миграции
- Команда `python manage.py migrate cards 0001` откатывает миграцию до определенной

### Shell plus
- `pip install ipython django-extensions` установка пакетов для работы с Django shell plus
- Добавьте `django_extensions` в список `INSTALLED_APPS` в вашем файле `settings.py`
- `python manage.py shell_plus` запуск Django shell plus
- `python manage.py shell_plus --print-sql` показывает SQL запросы

#### Работа с Django shell plus
1. Мы установили и запустили Django shell plus
2. Создали модель Card
3. Сделали миграцию
4. Применили миграцию
---
Теперь мы можем создавать записи в БД и работать с ними через Python код
т.к. это shell plus - нам ничего не надо импортировать, все модули уже подгружены

##### CRUD
1. Создаем объект карточки
`card = Card(question='Что такое PEP 8?', answer='PEP 8 — стандарт написания кода на Python.')`
`card.save()` # Сохраняем карточку в БД

2. Ищем карточку по id 1
`card = Card.objects.get(id=1)`

3. Изменяем карточку которая лежит в переменной card
`card.question = "Что такое PEP 8?"`
`card.answer = "PEP 8 — стандарт написания кода на Python."`
`card.save()` # Сохраняем изменения

4. Удаляем карточку
`card.delete()`
Но если мне нужно её найти то
`Card.objects.get(id=1).delete() `

#### Работа с несколькими объектами
Мы можем создать сразу несколько объектов bulk_create
```python
cards = (
    Card(question="Что такое PEP 8?", answer="PEP 8 — стандарт написания кода на Python."),
    Card(question="Что такое PEP 20?", answer="PEP 20 — The Zen of Python."),
    Card(question="Питон или Пайтон?", answer="Пайтон."),
    )
```
`Card.objects.bulk_create(cards)`

Получить все карточки
`cards = Card.objects.all()`

Получить первых 2 карточки LIMIT 2
`cards = Card.objects.all()[:2]` - это не работает в SHELL

Получить карточки в которых в ответах есть слово "PEP"
`cards = Card.objects.filter(answer__contains="PEP")`

Получить карточки в которых вопросы начинаются на "Что такое PEP"
`cards = Card.objects.filter(question__startswith="Что такое PEP")`
"""


### Добавили первое представление из БД
cards/<int:card_id>/detail/
Добавили `get_object_or_404` для обработки ошибок 404

### Представление, которое обрабатывает `get` запросы (экспериментальный catalog2)
- Создаем новый маршрут `catalog2` в `cards.urls`
- path('catalog2/', views.catalog2, name='catalog2')
- Создаем новое представление `catalog2` в `views.py`
- Добавляем в `catalog2` обработку `get` запросов

## Lesson 59:
16.03.2024
### Разбор HW_37

- Подключение модели `Card` в админку
- Руссификация админки
- Создание суперпользователя через команду `python manage.py createsuperuser`
- Посмотрели на CRUD операции в админке

### Типы связей в моделях Django

#### Один к одному (OneToOneField)
Начали разбирать пример, но столкнулись с `User` - моделью Django, которая уже используется
Джанго, пришлось переделывать это в `User_custom` и откатывать миграции

#### Один ко многим (ForeignKey)
- Создали модели `Post` и `Comment` и связали их через `ForeignKey`
- Создали миграции и применили их
- Создали записи и выбрали их через связь


## Lesson 61:
- Разбор домашнего задания
- Работа с админ-панелью
- Руссификация админ-панели через `settings.py` и `LANGUAGE_CODE = 'ru'`
- Руссификация подписи групп моделей приложения в админке
- Руссификация названий моделей в единственном и множественном числе
- Добавление моделей в админ-панель
- Добавления фильтра по категориям
- Добавление поиска по всем полям
- Добавление кастомного поля через `@admin.display(description="Краткое описание", ordering='answer')`
что позволяет добавить кастомное поле в админке (есть ли код + длина ответа) с сортировкой по ответу
- Добавление кастомного фильтра по критерию `is_checked` через `list_filter` аттрибут
- Модификация модели `Card` - добавление поля `is_checked` и `IntegerChoices`
- Добавление костыля для трансформации `IntegerChoices` в `BooleanField` в поле


## Lesson 62:
- Руссификация фильтра в админке, через создание класса фильтра (наследник `admin.SimpleListFilter`)
- Руссификация заголовка фильтра категории через `verbose_name` в поле модели
- Добавление рекдатирования статуса карточки, прямо в списке карточек (пока не работает)
- Добавили собственное действие в админке для карточек через `actions` `@admin.action(description='Отметить как проверенные')`

- Django Debug Toolbar
- Установка Django Debug Toolbar через `pip install django-debug-toolbar`
- Подключили Django Debug Toolbar через `settings.py` и `urls.py`

Следующие изменения:

urls.py
import debug_toolbar
from django.conf import settings
```python
if settings.DEBUG:
    urlpatterns = [
                      path('__debug__/', include(debug_toolbar.urls)),
                      # другие URL-паттерны
                  ] + urlpatterns

```

settings.py
```python
INSTALLED_APPS = [
    # другие приложения
    'debug_toolbar',
]

MIDDLEWARE = [
    # другие middleware
    'debug_toolbar.middleware.DebugToolbarMiddleware',
]

INTERNAL_IPS = [
         # ...
         '127.0.0.1',
         # ...
     ]
```

- Использовали жадную загрузку данных в `catalog` через `Card.objects.prefetch_related('tags').order_by(order_by)`
что дало жадную загрузку как всех карточек, так и их тегов. Для каталога, это ускорение загрузки в 15 раз
и 3 запроса против 450 + запросов

- `prefetch_related` - жадная загрузка для связанных объектов с отношением `ForeignKey` и `ManyToManyField`
- `select_related` - жадная загрузка для связанных объектов с отношением `OneToOneField` и `ForeignKey`


- Установили `django-jazzmin` через `pip install django-jazzmin`
- Подключили `django-jazzmin` через `settings.py`
- Добавили `jazzmin` в `INSTALLED_APPS`
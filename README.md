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
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
- Создн url для `index` в  `aniki` в `urls.py`
- Получили свой первый `HttpResponse` в браузере "Hello, World!"
- Для того чтобы убрать ошибки импорта в `urls.py` ищем в какой папке `manage.py` и Отмечаем ее как `source root` в PyCharm
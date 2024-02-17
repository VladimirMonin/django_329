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

### Пользователи

1. **Регистрация пользователя**: `/users/register/` - страница для регистрации новых пользователей.

2. **Авторизация пользователя**: `/users/login/` - страница для входа в систему существующих пользователей через email и пароль или через ВКонтакте.

3. **Восстановление доступа (сброс пароля)**: `/users/password_reset/` - начало процесса восстановления доступа, включая ввод email для отправки инструкций по сбросу пароля.

4. **Смена пароля**: `/users/password_change/` - страница для смены пароля авторизованным пользователями.

5. **Личный кабинет пользователя**: `/users/profile/<user_id>/` - страница личного кабинета пользователя, где он может повторять карточки и настраивать свой профиль.

6. **Просмотр профиля другого пользователя**: `/users/profile/<user_id>/view` - страница для просмотра профилей других пользователей с информацией о добавленных карточках и основных данных пользователя.

### Карточки

1. **Категории карточек**: `/cards/categories/` - страница со списком категорий карточек.

2. **Карточки по категории**: `/cards/categories/<category_slug>/` - отображение карточек определенной категории.

3. **Теги карточек**: `/cards/tags/<tag_slug>/` - отображение карточек, отмеченных определенным тегом.

4. **Статистика по карточке**: `/cards/<kart_id>/statistics/` - страница со статистикой по конкретной карточке, включая просмотры, добавления в избранное, количество повторений, дату добавления и автора.

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

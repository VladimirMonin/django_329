"""
Lesson 59 - Отдельная ветка для экспериментов с моделями
# Для запуска shell plus с отображением команд, надо выполнить: python manage.py shell_plus --print-sql
blank=True - позволяет полю быть пустым
null=True - позволяет полю быть null
откатится к миграции - python manage.py migrate cards 0001
"""
from django.db import models


class Card(models.Model):
    question = models.CharField(max_length=255)
    answer = models.TextField(max_length=5000)
    upload_date = models.DateTimeField(auto_now_add=True)
    views = models.IntegerField(default=0)
    adds = models.IntegerField(default=0)
    tags = models.JSONField(null=True)

    class Meta:
        db_table = 'Cards'
        verbose_name = 'Карточка'
        verbose_name_plural = 'Карточки'

    def __str__(self):
        return f'Карточка {self.question} - {self.answer[:50]}'


# Определение модели User
class User_custom(models.Model):
    username = models.CharField(max_length=150, unique=True)
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=30, blank=True)

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return self.username


# Определение модели Passport
class Passport(models.Model):
    user = models.OneToOneField(User_custom, on_delete=models.CASCADE)
    passport_number = models.CharField(max_length=9)
    issue_date = models.DateField()
    expiration_date = models.DateField()

    class Meta:
        verbose_name = 'Паспорт'
        verbose_name_plural = 'Паспорта'

    def __str__(self):
        return f"{self.passport_number} issued for {self.user.username}"


"""
#### Взаимодействие с данными
from your_app.models import User, Passport
from datetime import date

# Создание пользователя
user = User(username='john_doe', email='john@example.com', first_name='John', last_name='Doe')
user.save()

# Создание паспорта для пользователя
passport = Passport(user=user, passport_number='123456789', issue_date=date(2020, 1, 1), expiration_date=date(2030, 1, 1))
passport.save()

Вы можете легко получить доступ к паспортным данным пользователя и наоборот:
```python
# Получение пользователя по pk
user = User_custom.objects.get(pk=1)

# Получение pk его паспорта
passport_pk = user.passport.pk

# Получение номера паспорта
passport_number = user.passport.passport_number

# Получение паспорта пользователя
passport = user.passport

passport = Passport.objects.get(pk=passport_pk)

# Получение пользователя по паспорту
user = passport.user
```

Вы также можете использовать обратный доступ к связанным объектам:

```python
# Получение всех пользователей с их паспортами
users_with_passports = User.objects.select_related('passport')

for user in users_with_passports:
    print(user.username, user.passport.passport_number)
```

"""
"""
Lesson 57 - начали осваивать Django ORM

ID - Django сделает автоматом, он будет первичным ключом, индексом и автоинкрементом
Отличие charfield от textfield - в количестве символов, которые можно в них хранить
Charfield - до 255 символов, textfield - без ограничений

class Meta - это вложенный класс, который содержит метаданные модели
db_table - это имя таблицы в базе данных
verbose_name - это имя модели в единственном числе
verbose_name_plural - это имя модели во множественном числе
они используются для отображения в админке
"""
from django.db import models


class Card(models.Model):
    question = models.CharField(max_length=255)
    answer = models.TextField(max_length=5000)
    upload_date = models.DateTimeField(auto_now_add=True)
    views = models.IntegerField(default=0)
    adds = models.IntegerField(default=0)

    class Meta:
        db_table = 'Cards'
        verbose_name = 'Карточка'
        verbose_name_plural = 'Карточки'

    def __str__(self):
        return f'Карточка {self.question} - {self.answer[:50]}'


"""
1. Мы установили и запустили Django shell plus
2. Создали модель Card
3. Сделали миграцию
4. Применили миграцию
---
Теперь мы можем создавать записи в БД и работать с ними через Python код
т.к. это shell plus - нам ничего не надо импортировать, все модули уже подгружены

CRUD
1. Создаем объект карточки
card = Card(question='Что такое PEP 8?', answer='PEP 8 — стандарт написания кода на Python.')
card.save() # Сохраняем карточку в БД

2. Ищем карточку по id 1
card = Card.objects.get(id=1)

3. Изменяем карточку которая лежит в переменной card
card.question = "Что такое PEP 8?"
card.answer = "PEP 8 — стандарт написания кода на Python."
card.save() # Сохраняем изменения

4. Удаляем карточку
card.delete()
Но если мне нужно её найти то
Card.objects.get(id=1).delete() 
"""
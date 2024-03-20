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
    card_id = models.AutoField(primary_key=True, db_column='CardID')
    question = models.TextField(db_column='Question')
    answer = models.TextField(db_column='Answer')
    category_id = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, db_column='CategoryID')
    upload_date = models.DateTimeField(auto_now_add=True, db_column='UploadDate')
    views = models.IntegerField(default=0, db_column='Views')
    favorites = models.IntegerField(default=0, db_column='Favorites')
    # Непосредственное определение связи многие ко многим с моделью Tag
    tags = models.ManyToManyField('Tag', related_name='cards', through='CardTags')

    # through - это модель, которая будет использоваться для связи многие ко многим

    class Meta:
        db_table = 'Cards'
        verbose_name = 'Карточка'
        verbose_name_plural = 'Карточки'

    def __str__(self):
        return f'Карточка {self.question} - {self.answer[:50]}'


class CardTags(models.Model):
    card = models.ForeignKey('Card', on_delete=models.CASCADE, db_column='CardID')
    tag = models.ForeignKey('Tag', on_delete=models.CASCADE, db_column='TagID')

    class Meta:
        db_table = 'CardTags'
        unique_together = (('card', 'tag'),)

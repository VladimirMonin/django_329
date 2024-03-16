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
# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


# Модель пользователя
class User(models.Model):
    # Уберем blank=True, null=True для первичного ключа, т.к. это не соответствует логике первичного ключа
    user_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=255)

    class Meta:
        db_table = 'Users'


# Модель категорий
class Category(models.Model):
    category_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, unique=True)

    class Meta:
        db_table = 'Categories'


# Модель тегов
class Tag(models.Model):
    tag_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, unique=True)

    class Meta:
        db_table = 'Tags'


# Модель карточек
class Card(models.Model):
    card_id = models.AutoField(primary_key=True)
    question = models.TextField()
    answer = models.TextField()
    user = models.ForeignKey(User, on_delete=models.SET_DEFAULT, default=1)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    upload_date = models.DateTimeField(auto_now_add=True)
    views = models.IntegerField(default=0)
    adds = models.IntegerField(default=0)
    # Непосредственное определение связи многие ко многим с моделью Tag
    tags = models.ManyToManyField('Tag', related_name='cards')

    class Meta:
        db_table = 'Cards'

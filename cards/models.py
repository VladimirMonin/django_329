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
from django.contrib.auth.models import User
# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Category(models.Model):
    category_id = models.AutoField(primary_key=True, db_column='CategoryID')
    name = models.CharField(max_length=255, unique=True, db_column='Name')

    class Meta:
        db_table = 'Categories'


class Tag(models.Model):
    tag_id = models.AutoField(primary_key=True, db_column='TagID')
    name = models.CharField(max_length=255, unique=True, db_column='Name')

    class Meta:
        db_table = 'Tags'


class Card(models.Model):
    card_id = models.AutoField(primary_key=True, db_column='CardID')
    question = models.TextField(db_column='Question')
    answer = models.TextField(db_column='Answer')
    user_id = models.ForeignKey(User, on_delete=models.SET_DEFAULT, default=1, db_column='UserID')
    category_id = models.ForeignKey(Category, on_delete=models.SET_DEFAULT, default=1, db_column='CategoryID')
    upload_date = models.DateTimeField(auto_now_add=True, db_column='UploadDate')
    views = models.IntegerField(default=0, db_column='Views')
    favorites = models.IntegerField(default=0, db_column='Favorites')
    # Непосредственное определение связи многие ко многим с моделью Tag
    tags = models.ManyToManyField('Tag', related_name='cards', through='CardTags')

    # through - это модель, которая будет использоваться для связи многие ко многим

    class Meta:
        db_table = 'Cards'


class CardTags(models.Model):
    card = models.ForeignKey('Card', on_delete=models.CASCADE, db_column='CardID')
    tag = models.ForeignKey('Tag', on_delete=models.CASCADE, db_column='TagID')

    class Meta:
        db_table = 'CardTags'
        unique_together = (('card', 'tag'),)

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


class Cardtags(models.Model):
    cardid = models.OneToOneField('Cards', models.DO_NOTHING, db_column='CardID', primary_key=True, blank=True, null=True)  # Field name made lowercase. The composite primary key (CardID, TagID) found, that is not supported. The first column is selected.
    tagid = models.ForeignKey('Tags', models.DO_NOTHING, db_column='TagID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CardTags'


class Cards(models.Model):
    cardid = models.AutoField(db_column='CardID', primary_key=True, blank=True, null=True)  # Field name made lowercase.
    question = models.TextField(db_column='Question')  # Field name made lowercase.
    answer = models.TextField(db_column='Answer')  # Field name made lowercase.
    userid = models.ForeignKey('Users', models.DO_NOTHING, db_column='UserID', blank=True, null=True)  # Field name made lowercase.
    categoryid = models.ForeignKey('Categories', models.DO_NOTHING, db_column='CategoryID', blank=True, null=True)  # Field name made lowercase.
    uploaddate = models.DateTimeField(db_column='UploadDate', blank=True, null=True)  # Field name made lowercase.
    views = models.IntegerField(db_column='Views', blank=True, null=True)  # Field name made lowercase.
    favorites = models.IntegerField(db_column='Favorites', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Cards'


class Categories(models.Model):
    categoryid = models.AutoField(db_column='CategoryID', primary_key=True, blank=True, null=True)  # Field name made lowercase.
    name = models.TextField(db_column='Name', unique=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Categories'


class Tags(models.Model):
    tagid = models.AutoField(db_column='TagID', primary_key=True, blank=True, null=True)  # Field name made lowercase.
    name = models.TextField(db_column='Name', unique=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Tags'


class Users(models.Model):
    userid = models.AutoField(db_column='UserID', primary_key=True, blank=True, null=True)  # Field name made lowercase.
    firstname = models.TextField(db_column='FirstName')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Users'

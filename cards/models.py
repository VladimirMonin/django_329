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

model.choice - это класс, который позволяет создавать поля с ограниченным набором значений
варианты integerchoices и charchoices
"""
from django.db import models
from django.urls import reverse
import logging

# Создаем или получаем экземпляр логгера
logger = logging.getLogger(__name__)

# Устанавливаем базовый уровень логирования. В продакшене вы можете выбрать уровень WARNING или ERROR
logging.basicConfig(level=logging.DEBUG)


class Category(models.Model):
    category_id = models.AutoField(primary_key=True, db_column='CategoryID')
    name = models.CharField(max_length=255, unique=True, db_column='Name')

    class Meta:
        db_table = 'Categories'
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name


class Tag(models.Model):
    tag_id = models.AutoField(primary_key=True, db_column='TagID')
    name = models.CharField(max_length=255, unique=True, db_column='Name')

    class Meta:
        db_table = 'Tags'
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'

    def __str__(self):
        return self.name


class Card(models.Model):
    class Status(models.IntegerChoices):
        UNCHECKED = 0, 'Не проверено'
        CHECKED = 1, 'Проверено'

    card_id = models.AutoField(primary_key=True, db_column='CardID')
    question = models.TextField(db_column='Question')
    answer = models.TextField(db_column='Answer')
    category_id = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, db_column='CategoryID', verbose_name='Категория')
    upload_date = models.DateTimeField(auto_now_add=True, db_column='UploadDate', verbose_name='Дата загрузки')
    views = models.IntegerField(default=0, db_column='Views')
    favorites = models.IntegerField(default=0, db_column='Favorites')
    # Через map bool мы будем приводить 0 и 1 к False и True
    check_status = models.BooleanField(choices=tuple(map(lambda x: (bool(x[0]), x[1]), Status.choices)),
                                       default=Status.UNCHECKED, db_column='CheckStatus')
    # Непосредственное определение связи многие ко многим с моделью Tag
    tags = models.ManyToManyField('Tag', related_name='cards', through='CardTags')

    # through - это модель, которая будет использоваться для связи многие ко многим

    class Meta:
        db_table = 'Cards'
        verbose_name = 'Карточка'
        verbose_name_plural = 'Карточки'

    def __str__(self):
        return self.question

    # Опишем get_absolute_url для модели Card - метод, который возвращает URL карточки
    # Псевдоним - detail_card_by_id
    # reverse - возвращает URL по псевдониму
    def get_absolute_url(self):
        return reverse('detail_card_by_id', kwargs={'card_id': self.card_id})

    def save(self, *args, **kwargs):
        # Логируем перед сохранением объекта
        logger.debug(f'Сохранение карточки {self.card_id}, значения: {self.__dict__}')

        super().save(*args, **kwargs)  # Вызываем оригинальный метод save


class CardTags(models.Model):
    id = models.AutoField(primary_key=True, db_column='id')
    card = models.ForeignKey('Card', on_delete=models.CASCADE, db_column='CardID')
    tag = models.ForeignKey('Tag', on_delete=models.CASCADE, db_column='TagID')

    class Meta:
        db_table = 'CardTags'
        unique_together = (('card', 'tag'),)
        verbose_name = 'Связь карточка-тег'
        verbose_name_plural = 'Связи карточка-тег'

    def __str__(self):
        return f'{self.card} - {self.tag}'

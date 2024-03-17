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
    tags = models.ManyToManyField('Tag', related_name='cards', null=True)

    class Meta:
        db_table = 'Cards'
        verbose_name = 'Карточка'
        verbose_name_plural = 'Карточки'

    def __str__(self):
        return f'Карточка {self.question} - {self.answer[:50]}'


class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)

    class Meta:
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'

    def __str__(self):
        return self.name




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


# Определение модели Post
class Post(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField()

    def __str__(self):
        return self.title


# Определение модели Comment
class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    author_name = models.CharField(max_length=50)
    text = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comment by {self.author_name} on {self.post.title}"


"""
Запросы в Shell Plus
1. Добавить пост

from cards.models import Post
post = Post(title='Первый пост', body='Тело первого поста')

2. Сохранить пост
post.save()

3. Добавить комментарий
from cards.models import Comment
comment = Comment(post=post, author_name="Вася", text="Текст комментария")
comment = Comment(post=post, author_name="Вова", text="Текст комментария 2")
comment.save()

Найдем первый коммент Василия
comment = Comment.objects.filter(author_name="Вася").first()

Найдем все комменты к этому посту
comments = Comment.objects.filter(post=post)

Сортируем посты по имени автора desc
comments = Comment.objects.order_by("-author_name")
"""
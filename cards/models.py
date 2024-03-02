"""
Lesson 57 - начали осваивать Django ORM

ID - Django сделает автоматом, он будет первичным ключом, индексом и автоинкрементом
Отличие charfield от textfield - в количестве символов, которые можно в них хранить
Charfield - до 255 символов, textfield - без ограничений
"""
from django.db import models


class Card(models.Model):
    question = models.CharField()
    answer = models.TextField(max_length=5000)
    upload_date = models.DateTimeField(auto_now_add=True)
    views = models.IntegerField(default=0)
    adds = models.IntegerField(default=0)


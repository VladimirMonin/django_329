from django import forms

from cards.models import Category, Card, Tag


class CardModelForm(forms.ModelForm):
    # Определяем поля формы, связываем с моделью Card и добавляем дополнительные настройки
    category = forms.ModelChoiceField(queryset=Category.objects.all(), empty_label="Категория не выбрана",
                                      label='Категория')
    tags = forms.CharField(label='Теги', required=False, help_text='Перечислите теги через запятую')

    class Meta:
        model = Card
        fields = ['question', 'answer', 'category', 'tags']
        widgets = {
            'question': forms.TextInput(attrs={'class': 'form-control'}),
            'answer': forms.Textarea(attrs={'class': 'form-control', 'rows': 4, 'cols': 40}),
            'category': forms.Select(attrs={'class': 'form-control'}),
            'tags': forms.TextInput(attrs={'class': 'form-control'}),
        }
        labels = {
            'question': 'Вопрос',
            'answer': 'Ответ',
        }

    def clean_tags(self) -> list:
        # Валидация и преобразование строки тегов в список тегов
        tags_str = self.cleaned_data['tags']
        tag_list = [tag.strip() for tag in tags_str.split(',') if tag.strip()]
        return tag_list

    def save(self, *args, **kwargs):
        # Сохранение карточки вместе с тегами
        # commit=False - отключает сохранение формы, чтобы мы могли добавить теги
        # instance = super().save(commit=False) # Получаем экземпляр модели Card , без сохранения в базу
          # Но сохраняем в базу, потому что многие-ко-многим нуждаются в ID

        # Обрабатываем теги
        tag_names = self.cleaned_data['tags']
        tag_objects = []
        for tag_name in tag_names:
            tag_name = tag_name.strip()
            if not tag_name:
                continue
            tag, _ = Tag.objects.get_or_create(name=tag_name)
            tag_objects.append(tag)

        # Добавляем теги к карточке
        self.tags = tag_objects
        instance = super().save(*args, **kwargs)
        return instance

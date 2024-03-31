from django import forms

from cards.models import Category, Card, Tag


class CardForm(forms.Form):
    question = forms.CharField(label='Вопрос', max_length=100, min_length=3, error_messages={'required': 'Поле не может быть пустым', 'min_length': 'Минимальная длина вопроса - 3 символа', 'max_length': 'Максимальная длина вопроса - 100 символов'})
    answer = forms.CharField(label='Ответ', min_length=10, widget=forms.Textarea(attrs={'rows': 10, 'cols': 30}), error_messages={'required': 'Поле не может быть пустым', 'min_length': 'Минимальная длина ответа - 10 символов'})
    category = forms.ModelChoiceField(queryset=Category.objects.all(), label='Категория', empty_label=None, required=True)


class CardModelForm(forms.ModelForm):
    # Определяем поля формы, связываем с моделью Card и добавляем дополнительные настройки
    category = forms.ModelChoiceField(queryset=Category.objects.all(), empty_label="Категория не выбрана", label='Категория')
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

    def clean_tags(self):
        # Валидация и преобразование строки тегов в список тегов
        tags_str = self.cleaned_data['tags']
        tag_list = [tag.strip() for tag in tags_str.split(',') if tag.strip()]
        return tag_list

    def save(self, *args, **kwargs):
        # Сохранение карточки вместе с тегами
        # commit=False - отключает сохранение формы, чтобы мы могли добавить теги
        # instance = super().save(commit=False) # Получаем экземпляр модели Card , без сохранения в базу
        instance = super().save() # Но сохраняем в базу, потому что многие-ко-многим нуждаются в ID

        # Обрабатываем теги
        tag_names = self.cleaned_data['tags']
        for tag_name in tag_names:
            tag_name = tag_name.strip()
            if not tag_name:
                continue
            tag, _ = Tag.objects.get_or_create(name=tag_name)
            instance.tags.add(tag)


        return instance
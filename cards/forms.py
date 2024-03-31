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

    def save(self, *args, **kwargs):
        # Сохраняем объект Card без коммита тегов, потому что для этого нужен ID объекта Card.
        instance = super().save(commit=False)
        instance.save()

        self.instance.tags.clear()  # Очищаем текущие теги, чтобы избежать дублирования

        # Обрабатываем теги
        tag_names = self.cleaned_data['tags'].split(',')
        for tag_name in tag_names:
            tag_name = tag_name.strip()
            if tag_name:  # Проверяем, не пустая ли строка после удаления пробелов
                tag, created = Tag.objects.get_or_create(name=tag_name)
                self.instance.tags.add(tag)

        return instance


from django import forms

from cards.models import Category


class CardForm(forms.Form):
    question = forms.CharField(label='Вопрос', max_length=100, min_length=3, error_messages={'required': 'Поле не может быть пустым', 'min_length': 'Минимальная длина вопроса - 3 символа'})
    answer = forms.CharField(label='Ответ', min_length=10, widget=forms.Textarea(attrs={'rows': 10, 'cols': 30}), error_messages={'required': 'Поле не может быть пустым', 'min_length': 'Минимальная длина ответа - 10 символов'})
    category = forms.ModelChoiceField(queryset=Category.objects.all(), label='Категория', empty_label=None, required=True)
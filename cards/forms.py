from django import forms


class CardForm(forms.Form):
    question = forms.CharField(label='Вопрос', max_length=100)
    answer = forms.CharField(label='Ответ', widget=forms.Textarea(attrs={'rows': 10, 'cols': 30}))
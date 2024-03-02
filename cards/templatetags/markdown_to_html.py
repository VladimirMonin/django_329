"""
Пользовательский шаблонный тег для шаблонизатора Django,
который преобразует текст из формата Markdown в HTML.

Используется в следующих шаблонах:

1. cards/templates/cards/include/card_preview.html
2. cards/templates/cards/card_detail.html

template - это объект, который предоставляет доступ к библиотеке шаблонов Django.
template.Library - это класс, который предоставляет доступ к библиотеке тегов и фильтров Django.
@register.simple_tag - это декоратор, который регистрирует функцию в качестве простого тега шаблона.
name='markdown_to_html' - это имя тега, которое будет использоваться в шаблоне.
"""

from django import template

register = template.Library()


@register.simple_tag(name='markdown_to_html')
def markdown_to_html(markdown_text: str) -> str:
    """
    Преобразует текст из формата Markdown в HTML
    ЭТО УЧЕБНЫЙ ПРИМЕР БЕЗ РЕАЛЬНОГО ФУНКЦИОНАЛА

    :param markdown_text: Текст в формате Markdown
    :return: Текст в формате HTML
    """
    # Преобразование Markdown в HTML
    html_text = "ЭТО HTML!) " + markdown_text.upper()

    return html_text

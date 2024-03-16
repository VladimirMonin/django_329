"""
python manage.py createsuperuser - создание суперпользователя
"""

from django.contrib import admin

from .models import Card, User_custom, Passport


@admin.register(Card)
class CardAdmin(admin.ModelAdmin):
    pass


@admin.register(User_custom)
class UserAdmin(admin.ModelAdmin):
    search_fields = ('username', 'email')
    pass


@admin.register(Passport)
class PassportAdmin(admin.ModelAdmin):
    search_fields = ('passport_number', 'user__username',)
    pass

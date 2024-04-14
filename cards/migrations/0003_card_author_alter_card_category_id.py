# Generated by Django 4.2 on 2024-04-14 12:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('cards', '0002_alter_card_options_alter_cardtags_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='card',
            name='author',
            field=models.ForeignKey(db_column='AuthorID', default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='cards', to=settings.AUTH_USER_MODEL, verbose_name='Автор'),
        ),
        migrations.AlterField(
            model_name='card',
            name='category_id',
            field=models.ForeignKey(db_column='CategoryID', null=True, on_delete=django.db.models.deletion.SET_NULL, to='cards.category', verbose_name='Категория'),
        ),
    ]

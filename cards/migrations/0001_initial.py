# Generated by Django 4.2 on 2024-03-16 14:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Card',
            fields=[
                ('card_id', models.AutoField(db_column='CardID', primary_key=True, serialize=False)),
                ('question', models.TextField(db_column='Question')),
                ('answer', models.TextField(db_column='Answer')),
                ('upload_date', models.DateTimeField(auto_now_add=True, db_column='UploadDate')),
                ('views', models.IntegerField(db_column='Views', default=0)),
                ('favorites', models.IntegerField(db_column='Favorites', default=0)),
            ],
            options={
                'db_table': 'Cards',
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('category_id', models.AutoField(db_column='CategoryID', primary_key=True, serialize=False)),
                ('name', models.CharField(db_column='Name', max_length=255, unique=True)),
            ],
            options={
                'db_table': 'Categories',
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('tag_id', models.AutoField(db_column='TagID', primary_key=True, serialize=False)),
                ('name', models.CharField(db_column='Name', max_length=255, unique=True)),
            ],
            options={
                'db_table': 'Tags',
            },
        ),
        migrations.CreateModel(
            name='CardTags',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('card', models.ForeignKey(db_column='CardID', on_delete=django.db.models.deletion.CASCADE, to='cards.card')),
                ('tag', models.ForeignKey(db_column='TagID', on_delete=django.db.models.deletion.CASCADE, to='cards.tag')),
            ],
            options={
                'db_table': 'CardTags',
                'unique_together': {('card', 'tag')},
            },
        ),
        migrations.AddField(
            model_name='card',
            name='category_id',
            field=models.ForeignKey(db_column='CategoryID', default=1, on_delete=django.db.models.deletion.SET_DEFAULT, to='cards.category'),
        ),
        migrations.AddField(
            model_name='card',
            name='tags',
            field=models.ManyToManyField(related_name='cards', through='cards.CardTags', to='cards.tag'),
        ),
        migrations.AddField(
            model_name='card',
            name='user_id',
            field=models.ForeignKey(db_column='UserID', default=1, on_delete=django.db.models.deletion.SET_DEFAULT, to=settings.AUTH_USER_MODEL),
        ),
    ]

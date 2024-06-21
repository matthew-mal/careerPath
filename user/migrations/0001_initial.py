# Generated by Django 5.0.6 on 2024-06-20 12:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('user_type', models.PositiveSmallIntegerField(choices=[(1, 'Компания'), (2, 'Соискатель')], default=2, verbose_name='Тип пользователя')),
                ('username', models.CharField(max_length=255, verbose_name='Ф.И.О')),
                ('email', models.EmailField(max_length=254, verbose_name='Email')),
                ('phone_number', models.CharField(max_length=13, unique=True, verbose_name='Номер телефона')),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('updated_date', models.DateTimeField(auto_now=True, verbose_name='Дата обновления')),
                ('status', models.PositiveSmallIntegerField(choices=[(1, 'Обычный пользователь'), (2, 'Модератор')], default=1)),
                ('is_admin', models.BooleanField(default=False, verbose_name='Админ')),
                ('is_active', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'Пользователь',
                'verbose_name_plural': 'Все пользователи',
            },
        ),
    ]
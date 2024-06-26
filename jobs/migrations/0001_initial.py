# Generated by Django 5.0.6 on 2024-06-20 12:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, choices=[('Бэкенд - разработка', 'Бэкенд - разработка'), ('Фронтенд-разработка', 'Фронтенд-разработка'), ('Дизайн', 'Дизайн'), ('Тестирование и QA ', 'Тестирование и QA '), ('Администрирование и DevOps', 'Администрирование и DevOps'), ('Управление проектами', 'Управление проектами'), ('Аналитика и анализ данных', 'Аналитика и анализ данных')], default=None, max_length=250, null=True, verbose_name='Категория')),
                ('other_title', models.CharField(blank=True, max_length=250, null=True, verbose_name='Категория(другое)')),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категории',
            },
        ),
        migrations.CreateModel(
            name='Experience',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, choices=[('Стажер (Intern)', 'Стажер (Intern)'), ('Джуниор (Junior)', 'Джуниор (Junior)'), ('Мидл (Middle)', 'Мидл (Middle)'), ('Синьор (Senior)', 'Синьор (Senior)'), ('Ведущий (Lead)', 'Ведущий (Lead)'), ('Эксперт (Expert)', 'Эксперт (Expert)')], default=None, max_length=250, null=True, verbose_name='Опыт')),
                ('other_title', models.CharField(blank=True, max_length=250, null=True, verbose_name='Опыт(другое)')),
            ],
            options={
                'verbose_name': 'Опыт',
                'verbose_name_plural': 'Опыт',
            },
        ),
        migrations.CreateModel(
            name='Industry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, choices=[('Веб-разработка', 'Веб-разработка'), ('Мобильная разработка', 'Мобильная разработка'), ('Базы данных', 'Базы данных'), ('Кибербезопасность', 'Кибербезопасность'), ('Искусственный интеллект и машинное обучение', 'Искусственный интеллект и машинное обучение'), ('Сетевые технологии', 'Сетевые технологии'), ('IT-консалтинг', 'IT-консалтинг')], default=None, max_length=250, null=True, verbose_name='Отрасль')),
                ('other_title', models.CharField(blank=True, max_length=250, null=True, verbose_name='Отрасль(другое)')),
            ],
            options={
                'verbose_name': 'Отрасль',
                'verbose_name_plural': 'Отрасли',
            },
        ),
        migrations.CreateModel(
            name='Speciality',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, choices=[('Python-разработчик', 'Python-разработчик'), ('JavaScript-разработчик', 'JavaScript-разработчик'), ('Android-разработчик', 'Android-разработчик'), ('iOS-разработчик', 'iOS-разработчик'), ('Специалист по базам данных (DBA)', 'Специалист по базам данных (DBA)'), ('Исследователь данных', 'Исследователь данных'), ('Специалист по безопасности информации (InfoSec)', 'Специалист по безопасности информации (InfoSec)'), ('IT-консультант', 'IT-консультант'), ('Системный администратор', 'Системный администратор')], default=None, max_length=250, null=True, verbose_name='Специализация')),
                ('other_title', models.CharField(blank=True, max_length=250, null=True, verbose_name='Специализация(другое)')),
            ],
            options={
                'verbose_name': 'Специализация',
                'verbose_name_plural': 'Специализации',
            },
        ),
    ]

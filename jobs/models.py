from django.contrib.auth import get_user_model
from django.db import models

from .choices import IndustryCh, CategoryCh, SpecialityCh, ExperienceCh

User = get_user_model()

parametersForNull = {
    'null': True,
    'blank': True,
}


class Industry(models.Model):
    title = models.CharField(
        max_length=250,
        verbose_name='Отрасль',
        choices=IndustryCh,
        default=None,
        **parametersForNull
    )
    other_title = models.CharField(
        max_length=250,
        verbose_name='Отрасль(другое)',
        **parametersForNull
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Отрасль"
        verbose_name_plural = "Отрасли"


class Category(models.Model):
    title = models.CharField(
        max_length=250,
        verbose_name='Категория',
        choices=CategoryCh,
        default=None,
        **parametersForNull
    )
    other_title = models.CharField(
        max_length=250,
        verbose_name='Категория(другое)',
        **parametersForNull
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"


class Speciality(models.Model):
    title = models.CharField(
        max_length=250,
        verbose_name='Специализация',
        choices=SpecialityCh,
        default=None,
        **parametersForNull
    )
    other_title = models.CharField(
        max_length=250,
        verbose_name='Специализация(другое)',
        **parametersForNull
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Специализация"
        verbose_name_plural = "Специализации"


class Experience(models.Model):
    title = models.CharField(
        max_length=250,
        verbose_name='Опыт',
        choices=ExperienceCh,
        default=None,
        **parametersForNull
    )
    other_title = models.CharField(
        max_length=250,
        verbose_name='Опыт(другое)',
        **parametersForNull
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Опыт"
        verbose_name_plural = "Опыт"



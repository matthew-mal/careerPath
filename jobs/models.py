from django.contrib.auth import get_user_model
from django.db import models

from user.models import Employer
from .choices import IndustryCh, CategoryCh, SpecialityCh, ExperienceCh

User = get_user_model()

parameters_for_null = {
    'null': True,
    'blank': True,
}


class Industry(models.Model):
    title = models.CharField(
        max_length=250,
        verbose_name='Отрасль',
        choices=IndustryCh,
        default=None,
        **parameters_for_null
    )
    other_title = models.CharField(
        max_length=250,
        verbose_name='Отрасль(другое)',
        **parameters_for_null
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
        **parameters_for_null
    )
    other_title = models.CharField(
        max_length=250,
        verbose_name='Категория(другое)',
        **parameters_for_null
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
        **parameters_for_null
    )
    other_title = models.CharField(
        max_length=250,
        verbose_name='Специализация(другое)',
        **parameters_for_null
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
        **parameters_for_null
    )
    other_title = models.CharField(
        max_length=250,
        verbose_name='Опыт(другое)',
        **parameters_for_null
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Опыт"
        verbose_name_plural = "Опыт"


class Vacancy(models.Model):
    industry = models.ManyToManyField(
        Industry,
        verbose_name='Industry'
    )
    category = models.ManyToManyField(
        Category,
        verbose_name='Category'
    )
    specializing = models.ManyToManyField(
        Speciality,
        verbose_name='Speciality'
    )
    experience = models.ManyToManyField(
        Experience,
        verbose_name='Experience'
    )
    salary = models.DecimalField(
        decimal_places=2,
        max_digits=12,
        default=0.00,
        verbose_name='Salary'
    )
    location = models.CharField(
        max_length=255,
        verbose_name='Location'
    )
    company = models.ManyToManyField(
        Employer,
        verbose_name='Company'
    )
    published_date = models.DateTimeField(
        auto_now_add=True
    )
    status = models.BooleanField(
        default=False,
        verbose_name='status'
    )
    contacts = models.CharField(
        max_length=13,
        unique=True,
        verbose_name='Contacts'
    )

    def __str__(self):
        specializations = ', '.join([specialization.title for specialization in self.specializing.all()])
        categories = ', '.join([category.title for category in self.category.all()])
        industries = ', '.join([industry.title for industry in self.industry.all()])
        experiences = ', '.join([experience.title for experience in self.experience.all()])

        return f'{specializations}\n {categories}\n {industries}\n {experiences}'

    class Meta:
        verbose_name = "Vacancy"
        verbose_name_plural = "Vacancies"


class Response(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='User'
    )
    vacancy = models.ForeignKey(
        Vacancy,
        on_delete=models.CASCADE,
        verbose_name='Choose a vacancy'
    )
    cover_letter = models.TextField(
        verbose_name='Cover letter'
    )
    created_at = models.DateTimeField(
        auto_now_add=True)
    resume = models.FileField(
        upload_to="media/resume",
        verbose_name='Add your resume'
    )

    def __str__(self):
        return f'{self.user.username} responded to the vacancy :{self.vacancy}'

    class Meta:
        verbose_name = "Response"
        verbose_name_plural = "Responses"


class Chosen(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='User'
    )
    vacancy = models.ForeignKey(
        Vacancy,
        on_delete=models.CASCADE,
        verbose_name='Choose a vacancy'
    )
    created_date = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return f"{self.user} --> {self.vacancy}"

    class Meta:
        verbose_name = "Favourite"
        verbose_name_plural = "Favourites"

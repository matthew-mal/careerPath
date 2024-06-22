from django_filters import rest_framework as filters
from .models import Vacancy, Industry, Category, Speciality, Experience, Employer


class VacancyFilter(filters.FilterSet):
    """
    Filters for the Vacancy model.

    Allows filtering vacancies by minimum and maximum salary,
    industry, category, speciality, experience, company,
    location, published date, and status.
    """
    min_salary = filters.NumberFilter(field_name="salary", lookup_expr='gte')
    max_salary = filters.NumberFilter(field_name="salary", lookup_expr='lte')
    industry = filters.ModelMultipleChoiceFilter(queryset=Industry.objects.all())
    category = filters.ModelMultipleChoiceFilter(queryset=Category.objects.all())
    speciality = filters.ModelMultipleChoiceFilter(queryset=Speciality.objects.all())
    experience = filters.ModelMultipleChoiceFilter(queryset=Experience.objects.all())
    company = filters.ModelMultipleChoiceFilter(queryset=Employer.objects.all())
    location = filters.CharFilter(field_name="location", lookup_expr='icontains')
    published_date = filters.DateFilter(field_name="published_date", lookup_expr='date')
    status = filters.BooleanFilter(field_name="status")

    class Meta:
        model = Vacancy
        fields = [
            'min_salary',
            'max_salary',
            'industry',
            'category',
            'speciality',
            'experience',
            'company',
            'location',
            'published_date',
            'status'
        ]

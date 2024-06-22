from rest_framework import serializers
from .models import (Vacancy, Chosen, Response, Category, Industry, Speciality, Experience, Employer)


class CategoryListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'title', 'other_title')


class IndustryListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Industry
        fields = ('id', 'title', 'other_title')


class SpecialityListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Speciality
        fields = ('id', 'title', 'other_title')


class ExperienceListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Experience
        fields = ('id', 'title', 'other_title')


class EmployerListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employer
        fields = ('id', 'company_name', 'industry', 'other_industry', 'country', 'city')


class VacancyCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vacancy
        fields = (
            'id', 'industry', 'category', 'specializing', 'experience', 'salary', 'location', 'company',
            'published_date',
            'status', 'contacts')


class StatusListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vacancy
        fields = ('id', 'status')


class VacancyListSerializer(serializers.ModelSerializer):
    category = CategoryListSerializer(many=True)
    industry = IndustryListSerializer(many=True)
    specializing = SpecialityListSerializer(many=True)
    experience = ExperienceListSerializer(many=True)
    company = EmployerListSerializer(many=True)
    status = serializers.BooleanField()  # Directly using the boolean field

    class Meta:
        model = Vacancy
        fields = ('id', 'industry', 'category', 'specializing', 'experience', 'salary', 'status', 'location', 'company',
                  'published_date', 'contacts')


class ResponseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Response
        fields = ('id', 'user', 'vacancy', 'cover_letter', 'created_at', 'resume')


class ResponseCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Response
        fields = ('id', 'user', 'vacancy', 'cover_letter', 'created_at', 'resume')


class ChosenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chosen
        fields = ('id', 'user', 'vacancy', 'created_date')

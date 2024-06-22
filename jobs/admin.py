from django.contrib import admin
from .models import (
    Vacancy, Category, Industry, Chosen,
    Response, Speciality, Experience
)


@admin.register(Vacancy)
class VacancyAdmin(admin.ModelAdmin):
    list_display = ('id', 'salary', 'location', 'status', 'published_date', 'contacts')
    search_fields = ('location', 'contacts')
    list_filter = ('status', 'published_date')
    filter_horizontal = ('industry', 'category', 'specializing', 'experience', 'company')


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'other_title')
    search_fields = ('title', 'other_title')


@admin.register(Industry)
class IndustryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'other_title')
    search_fields = ('title', 'other_title')


@admin.register(Chosen)
class ChosenAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'vacancy', 'created_date')
    search_fields = ('user__username', 'vacancy__id')
    list_filter = ('created_date',)


@admin.register(Response)
class ResponseAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'vacancy', 'created_at')
    search_fields = ('user__username', 'vacancy__id')
    list_filter = ('created_at',)


@admin.register(Speciality)
class SpecialityAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'other_title')
    search_fields = ('title', 'other_title')


@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'other_title')
    search_fields = ('title', 'other_title')

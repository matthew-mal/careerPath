from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Employer, JobSeeker
from .forms import (
    EmployerCreationForm, EmployerChangeForm,
    JobSeekerCreationForm, JobSeekerChangeForm
)


class BaseUserAdmin(UserAdmin):
    """
    The base class for user admin.
    """
    list_display = ('username', 'email', 'phone_number', 'is_active', 'is_admin')
    list_filter = ('is_admin',)
    fieldsets = (
        (None, {'fields': ('password', 'username', 'phone_number', 'email')}),
        ('Permissions', {'fields': ('is_admin',)}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'phone_number', 'password1', 'password2'),
        }),
    )
    search_fields = ('phone_number', 'username', 'email')
    ordering = ('phone_number',)
    filter_horizontal = ()


class EmployerAdmin(BaseUserAdmin):
    form = EmployerChangeForm
    add_form = EmployerCreationForm


class JobSeekerAdmin(BaseUserAdmin):
    form = JobSeekerChangeForm
    add_form = JobSeekerCreationForm


admin.site.register(Employer, EmployerAdmin)
admin.site.register(JobSeeker, JobSeekerAdmin)

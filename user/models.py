from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models

from jobs.choices import IndustryCh, SpecialityCh

parameters_for_null = {
    'null': True,
    'blank': True,
}


class UserType(models.IntegerChoices):
    EMPLOYER = 1, "Employer"
    JOB_SEEKER = 2, "Job Seeker"


class MyUserManager(BaseUserManager):
    def create_user(self, phone_number, username, email, password=None):
        user = self.model(
            phone_number=phone_number,
            username=username,
            email=email
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, phone_number, username, email, password=None):
        user = self.create_user(
            phone_number=phone_number,
            username=username,
            email=email,
            password=password
        )
        user.is_superuser = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    user_type = models.PositiveSmallIntegerField(
        choices=UserType.choices,
        default=UserType.JOB_SEEKER,
        verbose_name="Type of the user"
    )
    username = models.CharField(
        max_length=255,
        verbose_name="Full name"
    )
    email = models.EmailField(
        verbose_name="Email"
    )
    phone_number = models.CharField(
        max_length=13,
        unique=True,
        verbose_name="Phone number"
    )
    created_date = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Date of creation"
    )
    updated_date = models.DateTimeField(
        auto_now=True,
        verbose_name="Update date"
    )
    status = models.PositiveSmallIntegerField(
        choices=(
            (1, 'Base user'),
            (2, 'Moderator')
        ),
        default=1
    )
    is_admin = models.BooleanField(
        default=False,
        verbose_name="Admin"
    )
    is_active = models.BooleanField(
        default=True
    )
    is_staff = models.BooleanField(
        default=False,
        verbose_name='Staff'
    )

    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"

    def __str__(self):
        return self.username

    objects = MyUserManager()

    USERNAME_FIELD = 'phone_number'
    REQUIRED_FIELDS = ['username', 'email']

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin


class Employer(User):
    company_name = models.CharField(
        verbose_name="Name of the company",
        max_length=255
    )
    industry = models.CharField(
        max_length=250,
        verbose_name='Name of the industry',
        choices=IndustryCh,
        **parameters_for_null
    )
    other_industry = models.CharField(
        max_length=250,
        verbose_name='Name of the industry(another)',
        **parameters_for_null
    )
    country = models.CharField(
        verbose_name="Country",
        max_length=255
    )
    city = models.CharField(
        verbose_name="City",
        max_length=255
    )

    class Meta:
        verbose_name = "Company"
        verbose_name_plural = "Companies"


class JobSeeker(User):
    speciality = models.CharField(
        choices=SpecialityCh,
        verbose_name="Your speciality",
        max_length=255,
        **parameters_for_null
    )
    other_speciality = models.CharField(
        verbose_name="Your speciality(another)",
        max_length=255,
        **parameters_for_null
    )

    class Meta:
        verbose_name = "Job seeker"
        verbose_name_plural = "Job seekers"

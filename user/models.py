from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models


class UserType(models.IntegerChoices):
    employers = 1, "Компания"
    job_seeker = 2, "Соискатель"


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
            password=password  # Добавляем пароль
        )
        user.is_superuser = True  # Устанавливаем значение is_superuser
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    user_type = models.PositiveSmallIntegerField(
        choices=UserType.choices,
        default=UserType.job_seeker,
        verbose_name="Тип пользователя"
    )
    username = models.CharField(
        max_length=255,
        verbose_name="Ф.И.О"
    )
    email = models.EmailField(
        verbose_name="Email"
    )
    phone_number = models.CharField(
        max_length=13,
        unique=True,
        verbose_name="Номер телефона"
    )
    # cover = models.ImageField(
    #     upload_to="media/cover",
    #     verbose_name="Ваше фото",
    #     **parametersForNull
    # )
    created_date = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Дата создания"
    )
    updated_date = models.DateTimeField(
        auto_now=True,
        verbose_name="Дата обновления"
    )
    status = models.PositiveSmallIntegerField(
        choices=(
            (1, 'Обычный пользователь'),
            (2, 'Модератор')
        ),
        default=1
    )
    is_admin = models.BooleanField(
        default=False,
        verbose_name="Админ"
    )
    is_active = models.BooleanField(
        default=True
    )
    is_staff = models.BooleanField(
        default=False,
        verbose_name='Персонал'
    )

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Все пользователи"

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

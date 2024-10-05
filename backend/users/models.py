import uuid

from django.contrib.auth.models import AbstractUser
from django.core.validators import MinLengthValidator
from django.db import models

from core.constants import (EMAIL_LENGTH_MAX, EMAIL_LENGTH_MIN,
                            MAX_LENGTH_NAME, MIN_LENGTH_NAME,
                            USERNAME_LENGTH)
from core.validators import name_validator, username_validator


class User(AbstractUser):
    """Модель User (пользователь)"""

    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
        verbose_name="ID"
    )
    username = models.CharField(
        max_length=USERNAME_LENGTH,
        unique=True,
        verbose_name="Логин пользователя",
        validators=[username_validator],
        error_messages={
            "unique": "Пользователь с таким логином уже существует"
        }
    )
    email = models.EmailField(
        max_length=EMAIL_LENGTH_MAX,
        validators=[MinLengthValidator(limit_value=EMAIL_LENGTH_MIN)],
        unique=True,
        verbose_name="Адрес электронной почты",
    )
    first_name = models.CharField(
        max_length=MAX_LENGTH_NAME,
        validators=[MinLengthValidator(limit_value=MIN_LENGTH_NAME),
                    name_validator],
        verbose_name="Имя",
        null=True,
        blank=True,
    )
    last_name = models.CharField(
        max_length=MAX_LENGTH_NAME,
        validators=[MinLengthValidator(limit_value=MIN_LENGTH_NAME),
                    name_validator],
        verbose_name="Фамилия",
        null=True,
        blank=True,
    )

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"
        ordering = ("username",)

    def __str__(self):
        return self.username

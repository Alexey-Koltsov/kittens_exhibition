import re
from re import search

from django.core.exceptions import ValidationError


def username_validator(username):
    """Валидация для поля 'Логин пользователя' модели User."""
    if username == "me":
        raise ValidationError("Нельзя использовать имя пользователя me")

    if not search(r"^[a-zA-Z0-9@.+-_]+$", username):
        raise ValidationError(
            "В логине Пользователя используются недопустимые символы"
        )


def name_validator(name):
    """Общий валидатор: Имя пользователя
    и Фамилия пользователя модели User."""

    if not re.match(r"^[A-Za-zА-Яа-яЁё0-9 -]+$", name):
        raise ValidationError("Поле может содержать символы алфавита, пробел, дефис")

from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from djoser.serializers import UserCreateSerializer, UserSerializer
from rest_framework import serializers

from .models import Breed

User = get_user_model()


class BreedSerializer(serializers.ModelSerializer):
    """
    Сериализатор для работы с моделью City.
    Сериализатор, предназначенный только для получения названий городов.
    Attributes:
        - Meta: Класс метаданных для определения модели и полей сериализатора.
    """

    class Meta:
        model = Breed
        fields = (
            "id",
            "name",
        )
        read_only_fields = (
            "id",
            "name",
        )

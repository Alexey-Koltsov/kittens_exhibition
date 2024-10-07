import datetime as dt

from django.contrib.auth import get_user_model
from rest_framework import serializers

from .models import Breed, Kitten
from users.serializers import CustomUserReadSerializer


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


class KittenSerializer(serializers.ModelSerializer):
    """
    Сериализатор для работы с моделью Kitten.
    Сериализатор, предназначенный только для получения экземпляров котят.
    Attributes:
        - Meta: Класс метаданных для определения модели и полей сериализатора.
    """

    owner = CustomUserReadSerializer(read_only=True)
    age = serializers.SerializerMethodField()

    def get_age(self, obj):
        months = ((dt.datetime.now().year - obj.birth_date.year) * 12 +
                  (dt.datetime.now().month - obj.birth_date.month))
        return months

    class Meta:
        model = Kitten
        fields = (
            "id",
            "name",
            "slug",
            "color",
            "birth_date",
            "age",
            "owner",
            "breed",
            "image",
            "description",
        )
        read_only_fields = (
            "id",
            "slug",
            "owner",
        )

from django_filters import rest_framework as filters

from .models import Breed, Kitten


class BreedFilter(filters.FilterSet):
    """
    Фильтрация для модели Breed.
    Attributes:
        name (CharFilter): Фильтр по началу названия породы.
    """

    name = filters.CharFilter(
        field_name="name",
        lookup_expr="istartswith"
    )

    class Meta:
        model = Breed
        fields = (
            "name",
        )


class KittenFilter(filters.FilterSet):
    """
    Фильтрация для модели Kitten.
    Attributes:
        breed (IDFilter): Фильтр по ID породы.
    """

    name = filters.CharFilter(
        field_name="breed",
    )

    class Meta:
        model = Kitten
        fields = (
            "breed",
        )

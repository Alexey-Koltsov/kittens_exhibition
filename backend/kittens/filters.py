from django_filters import rest_framework as filters

from .models import Breed


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

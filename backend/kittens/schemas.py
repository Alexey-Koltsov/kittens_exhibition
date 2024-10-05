from drf_spectacular.types import OpenApiTypes
from drf_spectacular.utils import extend_schema, OpenApiResponse, OpenApiExample
from rest_framework import status
from drf_spectacular.utils import (extend_schema, OpenApiParameter,
                                   OpenApiResponse)


breed_description_schema = {
    "tags": ["breeds (Работа с породами)"]
}


BREED_DJOSER_SCHEMA = {
    "list": extend_schema(
        **breed_description_schema,
        summary="Получить список всех пород "
        " (Доступно любому пользователю).",
        description="Получить список всех пород. Поддерживается возможность"
        " поиска пород по имени (name) с ограничением по минимальному "
        "количеству символов (два символа).",
        parameters=[
            OpenApiParameter(
                name="name",
                location=OpenApiParameter.QUERY,
                description=" поиск пород совпадением по началу имени и"
                " с ограничением по минимальному количеству символов"
                " (два символа).",
                required=False,
                type=str
            ),
        ]
    ),
    "retrieve": extend_schema(
        **breed_description_schema,
        summary="Получить информацию о пород по ID."
        " (Доступно любому пользователю).",
        description="Получить информацию о породе по ID."
        " Возвращает информацию о конкретном запрошенной породе!",
    ),
}

from drf_spectacular.types import OpenApiTypes
from drf_spectacular.utils import extend_schema, OpenApiResponse, OpenApiExample
from rest_framework import status
from drf_spectacular.utils import (extend_schema, OpenApiParameter,
                                   OpenApiResponse)


breed_description_schema = {
    "tags": ["breeds (Работа с породами)"]
}
kitten_description_schema = {
    "tags": ["kittens (Работа с котятами)"]
}


BREED_SCHEMA = {
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


KITTEN_SCHEMA = {
    "list": extend_schema(
        **kitten_description_schema,
        summary="Получить список всех котят (Доступно любому пользователю).",
        description="Получить список всех котят",
    ),
    "create": extend_schema(
        **kitten_description_schema,
        summary="Создание нового котёнка (Доступно любому пользователю).",
        description=(
            "Создать нового котёнка. При успешном создании котёнка, "
            "он будет доступен для использования."
        ),
        responses={
            201: OpenApiResponse(
                description="Котёнок успешно создан."
            ),
        },
    ),
    "partial_update": extend_schema(
        **kitten_description_schema,
        summary="Частичное обновление информации о котёнке. "
        "(Доступно только хозяину котёнка или админу).",
        description="Частично обновляет информацию о котёнке."
    ),
    "update": extend_schema(
        **kitten_description_schema,
        summary="Обновить информацию о котёнке полностью.  "
        "(Доступно только хозяину котёнка или админу).",
        description="Обновляет данные информацию о котёнке. "
    ),
    "destroy": extend_schema(
        **kitten_description_schema,
        summary="Удаляет текущего котёнка "
        "(Доступно только хозяину котёнка или админу).",
        description="Удаляет текущего котёнка.",
        responses={
            200: OpenApiResponse(
                description="Котёнок успешно удалён."
            ),
        },
    ),
    "retrieve": extend_schema(
        **kitten_description_schema,
        summary="Получить информацию о котёнке по ID. "
        "(Доступно любому пользователю).",
        description="Получить информацию о пользователе по ID. "
        "Возвращает информацию о конкретном запрошенном пользователе!",
    ),
    "me": extend_schema(
        **kitten_description_schema,
        summary="Получить информацию о котёнке, "
        "владелец которого текущий пользователь. "
        "(Доступно авторизованному пользователю).",
        description="Получить информацию о котёнке,"
        "владелец которого текущий пользователь.",
    ),
}

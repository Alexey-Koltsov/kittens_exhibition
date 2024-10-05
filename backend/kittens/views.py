from django.contrib.auth import get_user_model
from django_filters.rest_framework import DjangoFilterBackend
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_protect
from django.views.generic import View
from djoser.views import UserViewSet
from djoser import utils
from drf_spectacular.utils import extend_schema, extend_schema_view
from rest_framework import status, viewsets, mixins
from rest_framework.decorators import action
from rest_framework.exceptions import PermissionDenied
from rest_framework.parsers import MultiPartParser, FormParser, FileUploadParser, JSONParser
from rest_framework.permissions import AllowAny, IsAdminUser, IsAuthenticated
from rest_framework.response import Response
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)
from kittens.filters import BreedFilter
from kittens.models import Breed
from users.permissions import IsOwnerOrReadOnlyOrAdmin
from kittens.schemas import BREED_DJOSER_SCHEMA
from kittens.serializers import BreedSerializer  # KittenSerializer


User = get_user_model()


@extend_schema_view(**BREED_DJOSER_SCHEMA)
class BreedViewSet(viewsets.ModelViewSet):
    """
     Кастомный ViewSet для работы с городами.
     Этот ViewSet предоставляет эндпоинты для получения пород.
     Attributes:
     - queryset: Запрос, возвращающий всех пород.
     - serializer_class: Сериализатор, используемый для получения породы.
     - lookup_field: Имя поля в URL для поиска объекта (по умолчанию "pk").
    Methods:
     - list - Возвращает список всех пород.
     - retrieve - Возвращает информацию о конкретной породе.
    """

    http_method_names = (
        "get",
    )
    lookup_field = "pk"
    queryset = Breed.objects.all()
    serializer_class = BreedSerializer
    permission_classes = [AllowAny,]
    filter_backends = (DjangoFilterBackend,)
    filterset_class = BreedFilter
    filterset_fields = ("name",)

    def filter_queryset(self, queryset):
        """
        Фильтруем кверисет: если параметр "name" передается и
        количество символов в параметре "name" меньше двух символов,
        то возвращается пустой кверисет.
        """
        name = self.request.query_params.get("name", None)
        if name is None or (name is not None and len(name) >= 2):
            for backend in list(self.filter_backends):
                queryset = backend().filter_queryset(
                    self.request, queryset, self)
            return queryset
        return queryset.none()

    def list(self, request, *args, **kwargs):
        """
        Возвращает список названий всех городов.
        """

        return super().list(request, *args, **kwargs)

    def retrieve(self, request, *args, **kwargs):
        """
        Возвращает название конкретного города.
        """
        return super().retrieve(request, *args, **kwargs)

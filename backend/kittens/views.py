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
from kittens.filters import BreedFilter, KittenFilter
from kittens.models import Breed, Kitten
from kittens.permissions import IsKittenOwnerOrReadOnlyOrAdmin
from kittens.schemas import BREED_SCHEMA, KITTEN_SCHEMA, kitten_description_schema
from kittens.serializers import BreedSerializer, KittenSerializer


User = get_user_model()


@extend_schema_view(**BREED_SCHEMA)
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
        Возвращает список названий всех пород.
        """

        return super().list(request, *args, **kwargs)

    def retrieve(self, request, *args, **kwargs):
        """
        Возвращает название конкретной породы.
        """
        return super().retrieve(request, *args, **kwargs)


@extend_schema_view(**KITTEN_SCHEMA)
class KittenViewSet(viewsets.ModelViewSet):
    """
     Кастомный ViewSet для работы с городами.
     Этот ViewSet предоставляет эндпоинты для получения пород.
     Attributes:
     - queryset: Запрос, возвращающий всех пород.
     - serializer_class: Сериализатор, используемый для получения породы.
     - lookup_field: Имя поля в URL для поиска объекта (по умолчанию "pk").
    Methods:
     - list - Возвращает список всех пород.
     - retrieve - Возвращает информацию о конкретном котёнке.
     - create -  Создает нового котёнка.
     - update - Обновляет информацию о конкретном котёнке.
     - partial_update - Частично обновляет информацию о конкретном котёнке.
     - destroy - Удаляет конкретного котёнка.
    """

    lookup_field = "pk"
    serializer_class = KittenSerializer
    permission_classes = [AllowAny,]
    filter_backends = (DjangoFilterBackend,)
    filterset_class = KittenFilter
    permission_classes = (IsKittenOwnerOrReadOnlyOrAdmin,)
    parser_classes = (MultiPartParser, JSONParser,)
    queryset = Kitten.objects.all()

    @extend_schema(
        **kitten_description_schema,
        summary="Получаем котёнка текущего пользователя"
        "(Доступно: авторизованному пользователю).",
    )
    @action(
        methods=['get'],
        serializer_class=KittenSerializer,
        permission_classes=[IsAuthenticated],
        detail=False,
        url_path='me',
    )
    def kitten_profile(self, request):
        kitten = get_object_or_404(Kitten, owner=self.request.user)
        serializer = self.get_serializer(kitten)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def perform_create(self, serializer):
        user = self.request.user
        serializer.save(owner=user)

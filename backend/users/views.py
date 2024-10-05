from django.contrib.auth import get_user_model
from djoser.views import UserViewSet
from djoser import utils
from drf_spectacular.utils import extend_schema_view
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)
from users.permissions import IsOwnerOrReadOnlyOrAdmin
from users.schemas import (
    JWT_CREATE_SCHEMA,
    JWT_TOKEN_REFRESH_SCHEMA,
    JWT_TOKEN_VERIFY_SCHEMA,
    USERS_DJOSER_SCHEMA
)
from users.serializers import (
    CustomUserReadSerializer,
    CustomUserSerializer,
    CustomUserUpdateSerializer,
)


User = get_user_model()


@extend_schema_view(**USERS_DJOSER_SCHEMA)
class CustomUserViewSet(UserViewSet):
    """
     Кастомный ViewSet для работы с пользователями.
     Этот ViewSet предоставляет эндпоинты для управления пользователями,
     включая активацию и частичное обновление.
     Attributes:
     - queryset: Запрос, возвращающий все объекты User.
     - serializer_class: Сериализатор, используемый для преобразования
     данных пользователя.
     - lookup_field: Имя поля в URL для поиска объекта (по умолчанию "pk"
     для UUID).
     Permissions:
         - permission_classes: Список классов разрешений для ViewSet.
    Methods:
     - list - Возвращает список всех пользователей.
     - create -  Создает нового пользователя.
     - retrieve - Возвращает информацию о конкретном пользователе.
     - update - Обновляет информацию о конкретном пользователе.
     - partial_update -  Частично обновляет информацию о конкретном
     пользователе.
     - destroy -  Удаляет конкретного пользователя.
    """

    lookup_field = "pk"

    def get_queryset(self):
        """
        Получение всех пользователей.
        """
        queryset = User.objects.all()
        return queryset

    def get_serializer_class(self):
        """
        Выбор подходящего сериализатора на основе типа действия.
        """
        if self.action == "create":
            return CustomUserSerializer
        if self.action in ("partial_update", "update",):
            return CustomUserUpdateSerializer
        return CustomUserReadSerializer

    def get_permissions(self):
        """
        Возвращает соответствующие разрешения в зависимости от действия.
        """

        action_permissions = {
            "list": (AllowAny(),),
            "retrieve": (AllowAny(),),
            "create": (AllowAny(),),
            "update": (IsOwnerOrReadOnlyOrAdmin(),),
            "partial_update": (IsOwnerOrReadOnlyOrAdmin(),),
            "destroy": (IsOwnerOrReadOnlyOrAdmin(),),
        }
        return action_permissions.get(self.action, super().get_permissions())

    def list(self, request, *args, **kwargs):
        """
        Возвращает список всех пользователей.
        """

        return super().list(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        """
        Создает нового пользователя.
        """
        return super().create(request, *args, **kwargs)

    def retrieve(self, request, *args, **kwargs):
        """
        Возвращает информацию о конкретном пользователе.
        """
        return super().retrieve(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        """
        Обновляет информацию о конкретном пользователе.
        """
        return super().update(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        """
        Удаляет конкретного пользователя.
        """
        instance = self.get_object()
        user_id = instance.id

        if instance == request.user:
            utils.logout_user(self.request)
        self.perform_destroy(instance)

        return Response(
            {"message": "Пользователь успешно удален", "id": user_id},
            status=status.HTTP_204_NO_CONTENT
        )

    @action(["get"], detail=False)
    def me(self, request, *args, **kwargs):
        """
        Получение информации о текущем пользователе.
        """
        return super().me(request, *args, **kwargs)


@JWT_CREATE_SCHEMA
class CustomTokenCreateView(TokenObtainPairView):
    """
    Кастомный viewset для создания JWT-токена.
    """

    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)


@JWT_TOKEN_REFRESH_SCHEMA
class CustomTokenRefreshView(TokenRefreshView):
    """
    Viewset для обновления JWT-токена с помощью refresh_token.
    """

    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)


@JWT_TOKEN_VERIFY_SCHEMA
class CustomTokenVerifyView(TokenVerifyView):
    """
    Viewset для проверки(верификации) JWT-токена c помощью access_tokenНап.
    """

    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)

from rest_framework import permissions


class IsKittenOwnerOrReadOnlyOrAdmin(permissions.BasePermission):
    """
    Пользователь может редактировать только свои собственные объекты.
    """

    def has_permission(self, request, view):
        """
        Проверяем разрешения на уровне представлений(view)
        """

        # Если запрос на чтение, разрешаем доступ
        if request.method in permissions.SAFE_METHODS:
            return True

        # Проверяем, аутентифицирован ли пользователь
        if not request.user.is_authenticated:
            return False

        return True

    def has_object_permission(self, request, view, obj):
        """
        Проверяем разрешения на уровне объекта.
        """

        # Разрешить любые запросы на чтение.
        if request.method in permissions.SAFE_METHODS:
            return True

        # Разрешить редактирование объекта только автору или админу.
        return (
            request.user.is_authenticated
            and (
                obj.owner == request.user or
                request.user.is_staff)
        )

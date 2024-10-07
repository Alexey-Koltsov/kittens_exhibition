from django.contrib import admin
from django.contrib.auth import get_user_model

User = get_user_model()


class BaseAdminSettings(admin.ModelAdmin):
    """
    Базовая настройка панели администратора.
    Attributes:
        - empty_value_display: Значение для отображения при пустом поле.
        - list_filter: Поля для фильтрации в списке объектов.
    """

    empty_value_display = "-пусто-"


@admin.register(User)
class UsersAdmin(BaseAdminSettings):
    """
    Администратор пользователей.
    Предоставляет интерфейс для управления пользователями.
    Attributes:
        - inlines: Встраиваемые таблицы.
        - list_display: Поля для отображения в списке объектов.
        - list_display_links: Поля - ссылки на детальную информацию.
        - search_fields: Поля, по которым доступен поиск.
    """

    list_display = (
        "id",
        "username",
        "email",
        "first_name",
        "last_name",
    )
    list_display_links = ("email", "username", "first_name", "last_name",)
    search_fields = ("email", "username", "first_name", "last_name",)

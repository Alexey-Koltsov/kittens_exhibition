from django.contrib import admin

from .models import Breed, Kitten


class BaseAdminSettings(admin.ModelAdmin):
    """
    Базовая настройка панели администратора.
    Attributes:
        - empty_value_display: Значение для отображения при пустом поле.
        - list_filter: Поля для фильтрации в списке объектов.
    """

    empty_value_display = "-пусто-"


@admin.register(Breed)
class BreedAdmin(BaseAdminSettings):
    """
    Администратор пользователей.
    Предоставляет интерфейс для управления пользователями.
    Attributes:
        - inlines: Встраиваемые таблицы.
        - list_display: Поля для отображения в списке объектов.
        - list_display_links: Поля, являющиеся ссылками на детальную информацию.
        - search_fields: Поля, по которым доступен поиск.
    """

    list_display = (
        "id",
        "name",
    )
    list_display_links = ("id", "name")
    search_fields = ("id", "name")


@admin.register(Kitten)
class KittenAdmin(BaseAdminSettings):
    """
    Администратор пользователей.
    Предоставляет интерфейс для управления пользователями.
    Attributes:
        - inlines: Встраиваемые таблицы.
        - list_display: Поля для отображения в списке объектов.
        - list_display_links: Поля, являющиеся ссылками на детальную информацию.
        - search_fields: Поля, по которым доступен поиск.
    """

    list_display = (
        "id",
        "name",
        "slug",
        "color",
        "birth_date",
        "owner",
        "breed",
        "image",
    )
    list_display_links = ("id", "name", "slug", "color",
                          "birth_date", "owner", "breed",)
    search_fields = ("id", "name""slug", "color",
                     "birth_date", "owner", "breed",)

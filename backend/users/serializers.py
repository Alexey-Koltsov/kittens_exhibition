from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from djoser.serializers import UserCreateSerializer, UserSerializer
from rest_framework import serializers

User = get_user_model()


class CustomUserSerializer(UserCreateSerializer):
    """
    Сериализатор для создания пользователями.
    Сериализатор, расширяющий базовый сериализатор создания пользователя,
    для обработки дополнительных полей.
    Attributes:
        - Meta: Класс метаданных для определения модели и полей сериализатора.
    """

    username = serializers.CharField(min_length=2,
                                     max_length=50,
                                     required=True)
    email = serializers.EmailField(min_length=6,
                                   max_length=70,
                                   required=True)
    first_name = serializers.CharField(min_length=2,
                                       max_length=50,
                                       required=True)
    last_name = serializers.CharField(min_length=2,
                                      max_length=50,
                                      required=True)

    class Meta:
        model = User
        fields = (
            "id",
            "username",
            "email",
            "first_name",
            "last_name",
            "password",
        )
        extra_kwargs = {
            "username": {"required": True},
            "email": {"required": True},
            "first_name": {"required": True},
            "last_name": {"required": True},
            "password": {"write_only": True,
                         "required": True},
        }

    def create(self, validated_data):
        user = User(
            username=validated_data["username"],
            email=validated_data["email"],
            first_name=validated_data["first_name"],
            last_name=validated_data["last_name"],
            password=validated_data["password"],
        )
        user.set_password(validated_data["password"])
        user.save()
        return user

    def validate_email(self, value):
        if User.objects.filter(email=value).exists():
            raise serializers.ValidationError(
                "Пользователь с таким email уже существует"
            )
        return value

    def capitalize_first_last_name(self, name: str) -> str:
        """
        Делаем каждое слово с заглавной буквы.
        """
        name = name.replace("-", "- ")
        name_list: list[str] = name.split()
        name_list = [name.capitalize() for name in name_list]
        name = " ".join(name_list)
        name = name.replace("- ", "-")
        return name

    def validate_first_name(self, value):
        """
        Делаем первую букву слова в имени, отчества и фамилии в заглавную.
        """
        value = self.capitalize_first_last_name(value)
        return value

    def validate_last_name(self, value):
        """
        Делаем первую букву слова в имени, отчества и фамилии в заглавную.
        """
        value = self.capitalize_first_last_name(value)
        return value

    def update(self, instance, validated_data):
        """
        Обновление пользователя с валидацией из моделей.
        Запускаем полную проверку данных модели, вызывая метод full_clean()
        Исключения: serializers.ValidationError:
        Возникает при ошибке валидации на уровне модели.
        """
        instance.first_name = validated_data.get("first_name",
                                                 instance.first_name)
        instance.last_name = validated_data.get("last_name",
                                                instance.last_name)

        try:
            instance.full_clean()
        except ValidationError as e:
            raise serializers.ValidationError(e.message_dict)

        instance.save()
        return instance


class CustomUserUpdateSerializer(UserSerializer):
    """
    Сериализатор обновления пользователей.
    Используется для просмотра и обновления данных существующего пользователя.
    Атрибуты:
        - Meta: Класс метаданных для определения модели и полей сериализатора.
    """

    first_name = serializers.CharField(min_length=2, max_length=50)
    last_name = serializers.CharField(min_length=2, max_length=50)

    class Meta(UserSerializer.Meta):
        model = User
        fields = (
            "id",
            "username",
            "email",
            "first_name",
            "last_name",
        )
        read_only_fields = (
            "id",
            "username",
            "email",
        )

    def capitalize_first_last_name(self, name: str) -> str:
        """
        Делаем каждое слово с заглавной буквы.
        """
        name = name.replace("-", "- ")
        name_list: list[str] = name.split()
        name_list = [name.capitalize() for name in name_list]
        name = " ".join(name_list)
        name = name.replace("- ", "-")
        return name

    def validate(self, attrs):
        """
        Делаем первую букву слова в имени, отчества и фамилии в заглавную.
        """
        if "first_name" in attrs:
            first_name = attrs["first_name"]
            attrs["first_name"] = self.capitalize_first_last_name(first_name)
        if "last_name" in attrs:
            last_name = attrs["last_name"]
            attrs["last_name"] = self.capitalize_first_last_name(last_name)
        return attrs

    def update(self, instance, validated_data):
        """
        Обновление пользователя с валидацией из моделей.
        Запускаем полную проверку данных модели, вызывая метод full_clean()
        Исключения: serializers.ValidationError:
        Возникает при ошибке валидации на уровне модели.
        """
        instance.first_name = validated_data.get("first_name",
                                                 instance.first_name)
        instance.last_name = validated_data.get("last_name",
                                                instance.last_name)

        try:
            instance.full_clean()
        except ValidationError as e:
            raise serializers.ValidationError(e.message_dict)

        instance.save()
        return instance


class CustomUserReadSerializer(serializers.ModelSerializer):
    """
    Сериализатор для чтения пользователей.
    Сериализатор, предназначенный только для чтения данных пользователя.
    Attributes:
        - Meta: Класс метаданных для определения модели и полей сериализатора.
    """

    class Meta:
        model = User
        fields = (
            "id",
            "username",
            "email",
            "first_name",
            "last_name",
        )
        read_only_fields = (
            "id",
            "email",
            "username",
            "first_name",
            "last_name",
        )

from django.contrib.auth import get_user_model
from django.db import models
from pytils.translit import slugify

from core.constants import MAX_LENGTH_NAME
from core.validators import name_validator

User = get_user_model()


class Breed(models.Model):
    name = models.CharField(
        max_length=MAX_LENGTH_NAME,
        unique=True,
        verbose_name="Название породы",
        validators=[name_validator],
        error_messages={
            "unique": "Такая порода уже существует"
        }
    )

    class Meta:
        verbose_name = "Порода"
        verbose_name_plural = "Породы"
        ordering = ("name",)

    def __str__(self):
        return self.name


class Kitten(models.Model):
    name = models.CharField(
        max_length=MAX_LENGTH_NAME,
        verbose_name="Имя котенка",
        validators=[name_validator],
    )
    slug = models.SlugField(
        max_length=MAX_LENGTH_NAME,
        verbose_name="Слаг",
    )
    color = models.CharField(max_length=16)
    birth_date = models.DateField()
    owner = models.OneToOneField(
        User,
        on_delete=models.CASCADE
    )
    breed = models.ForeignKey(
        Breed,
        related_name="kittens",
        on_delete=models.CASCADE
    )
    image = models.ImageField(
        upload_to="images/",
    )

    class Meta:
        verbose_name = "Котёнок"
        verbose_name_plural = "Котята"
        ordering = ("name",)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        """
        Если слаг не добавлен, то он формируется и
        сохраняется автоматически
        """
        if not self.slug:
            max_slug_length = self._meta.get_field("slug").max_length
            self.slug = slugify(self.name)[:max_slug_length]
        super().save(*args, **kwargs)

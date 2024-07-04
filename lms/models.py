from django.db import models

from config import settings

NULLABLE = {"blank": True, "null": True}


class Well(models.Model):
    """
    Модель курса поля: название,описание,превью (картинка)
    """

    title = models.CharField(
        max_length=150,
        verbose_name="Название курса",
        help_text="Введите название курса",
    )
    description = models.CharField(
        max_length=300,
        verbose_name="Описание курса",
        help_text="Введите описание курса",
        **NULLABLE,
    )
    image = models.ImageField(
        upload_to="images/",
        verbose_name="Превью курса",
        help_text="Выберите картинку",
        **NULLABLE,
    )
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        **NULLABLE,
        verbose_name="Пользователь ",
    )

    def __str__(self):
        return f"{self.title} {self.description}"

    class Meta:
        verbose_name = "Курс"
        verbose_name_plural = "Курсы"
        ordering = ('title',)


class Lesson(models.Model):
    """
    Модель урока, содержит поля название,описание, курс, превью (картинка), ссылка на видео
    """

    title = models.CharField(
        max_length=150,
        verbose_name="Название урока",
        help_text="Введите название урока",
    )
    description = models.CharField(
        max_length=300,
        verbose_name="Описание урока",
        help_text="Введите описание урока",
        **NULLABLE,
    )
    well = models.ForeignKey(
        Well,
        on_delete=models.CASCADE,
        verbose_name="Курс",
        help_text="Выберите курс",
    )
    image = models.ImageField(
        upload_to="lms/",
        verbose_name="Превью курса",
        help_text="Выберите картинку",
        **NULLABLE,
    )
    url_video = models.URLField(
        verbose_name="Ссылка на видео", help_text="Добавьте ссылку на видео", **NULLABLE
    )
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        **NULLABLE,
        verbose_name="Пользователь ",
    )

    def __str__(self):
        return f"{self.title} {self.well}"

    class Meta:
        verbose_name = "Урок"
        verbose_name_plural = "Уроки"
        ordering = ('title',)


class Subscription(models.Model):
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        **NULLABLE,
        verbose_name="Пользователь",
    )
    well = models.ForeignKey(Well, on_delete=models.CASCADE, verbose_name="Курс")

    def __str__(self):
        return f"{self.owner}  {self.well}"

    class Meta:
        verbose_name = "Подписка"
        verbose_name_plural = "Подписки"

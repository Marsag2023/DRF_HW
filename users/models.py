from django.contrib.auth.models import AbstractUser
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

from lms.models import Well, Lesson

NULLABLE = {"null": True, "blank": True}


class User(AbstractUser):
    username = None
    email = models.EmailField(
        unique=True, verbose_name="Email", help_text="Введите адрес электронной почты"
    )
    avatar = models.ImageField(upload_to='users/', verbose_name='Аватар', **NULLABLE,
                               help_text='Загрузите свой аватар')
    phone = PhoneNumberField(
        verbose_name="Телефон", help_text="Введите номер телефона", **NULLABLE
    )
    tg_name = models.CharField(
        max_length=50,
        verbose_name="Имя в Telegram",
        **NULLABLE,
        help_text="Введите имя в Telegram"
    )
    city = models.CharField(
        max_length=50,
        verbose_name="Город",
        **NULLABLE,
        help_text="Введите город"
    )
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"


class Payment(models.Model):

    PAYMENT_METHOD_CHOICES = [
        ("CASH", "Наличными"),
        ("TRANSFER", "Перевод на счет"),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Пользователь")
    date_payment = models.DateField(verbose_name="Дата оплаты", help_text="Введите дату оплаты", **NULLABLE)
    well = models.ForeignKey(
        Well, on_delete=models.CASCADE, verbose_name="Курс", **NULLABLE, help_text="Введите название курса")
    lesson = models.ForeignKey(
        Lesson, on_delete=models.CASCADE, verbose_name="Урок", **NULLABLE, help_text="Введите название урока")
    price = models.PositiveIntegerField(verbose_name="Цена", help_text="Введите сумму")
    payment_method = models.CharField(max_length=30, choices=PAYMENT_METHOD_CHOICES, default="CASH",
                                      verbose_name="Способ оплаты", help_text="Введите способ оплаты")

    class Meta:
        verbose_name = "Платеж"
        verbose_name_plural = "Платежи"

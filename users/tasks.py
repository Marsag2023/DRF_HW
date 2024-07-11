from celery import shared_task
from django.utils import timezone
from users.models import User


@shared_task
def active_users():
    """
    Проверяет наличие неактивных пользователей и устанавливает для их флага is_active значение False.
    """
    data = timezone.now() - timezone.timedelta(days=30)
    users = User.objects.filter(last_login__lte=data, is_active=True)
    print(users)
    for user in users:
        user.is_active = False
        user.save()

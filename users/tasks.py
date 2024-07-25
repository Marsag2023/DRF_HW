from celery import shared_task
<<<<<<< HEAD
from dateutil.relativedelta import relativedelta
=======
>>>>>>> origin/main
from django.utils import timezone
from users.models import User


@shared_task
def active_users():
    """
<<<<<<< HEAD
    Проверяет наличие неактивных пользователей
    и устанавливает для их флага is_active значение False.
    """
    month_ago = timezone.now() - relativedelta(months=1)
    users = User.objects.filter(last_login__lte=month_ago, is_active=True)
    users.update(is_active=False, updated_fields=['is_active'])
=======
    Проверяет наличие неактивных пользователей и устанавливает для их флага is_active значение False.
    """
    data = timezone.now() - timezone.timedelta(days=30)
    users = User.objects.filter(last_login__lte=data, is_active=True)
    print(users)
    for user in users:
        user.is_active = False
        user.save()
>>>>>>> origin/main

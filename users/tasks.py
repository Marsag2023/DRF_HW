from celery import shared_task
from dateutil.relativedelta import relativedelta
from django.utils import timezone
from users.models import User


@shared_task
def active_users():
    """
    Проверяет наличие неактивных пользователей
    и устанавливает для их флага is_active значение False.
    """
    month_ago = timezone.now() - relativedelta(months=1)
    users = User.objects.filter(last_login__lte=month_ago, is_active=True)
    users.update(is_active=False, updated_fields=['is_active'])

from celery import shared_task
from django.core.mail import send_mail
from config import settings
from lms.models import Subscription


@shared_task
def send_mail_update(well_id):
    """
    Отправляет письма об изменении курса для подписчиков
    """
    for subscription in Subscription.objects.filter(well_id=well_id):
        send_mail(
            subject='Обновление курса',
            message=f'Курс "{subscription.well}" был обновлен.',
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[subscription.owner.email],
        )

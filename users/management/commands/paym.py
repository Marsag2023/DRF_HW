from django.core.management import BaseCommand

from lms.models import Lesson, Well
from users.models import Payment, User


class Command(BaseCommand):

    def handle(self, *args, **options):
        payment_list = [
            dict(
                user=User.objects.get(pk=4),
                date_payment="2024-06-20",
                well=Well.objects.get(pk=4),
                price=10000,
                payment_method="TRANSFER",
            ),
            dict(
                user=User.objects.get(pk=5),
                date_payment="2024-06-20",
                well=Well.objects.get(pk=5),
                price=10000,
                payment_method="TRANSFER",
            ),
            dict(
                user=User.objects.get(pk=6),
                date_payment="2024-06-20",
                lesson=Lesson.objects.get(pk=2),
                price=1000,
                payment_method="TRANSFER",
            ),
            dict(
                user=User.objects.get(pk=6),
                date_payment="2024-06-20",
                lesson=Lesson.objects.get(pk=1),
                price=1000,
                payment_method="TRANSFER",
            ),
            dict(
                user=User.objects.get(pk=7),
                date_payment="2024-06-20",
                lesson=Lesson.objects.get(pk=3),
                price=1000,
                payment_method="CASH",
            ),
            dict(
                user=User.objects.get(pk=7),
                date_payment="2024-06-20",
                lesson=Lesson.objects.get(pk=4),
                price=1000,
                payment_method="TRANSFER",
            ),
            dict(
                user=User.objects.get(pk=7),
                date_payment="2024-06-20",
                lesson=Lesson.objects.get(pk=2),
                price=1000,
                payment_method="CASH",
            ),
        ]
        payment_for_create = []
        for payment_item in payment_list:
            payment_for_create.append(Payment(**payment_item))

        Payment.objects.bulk_create(payment_for_create)

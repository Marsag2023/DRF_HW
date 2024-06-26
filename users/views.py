from rest_framework.generics import ListAPIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import AllowAny
from users.models import User, Payment
from users.serializer import UserSerializer, PaymentSerializer
from rest_framework import filters


class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_permissions(self):
        """
    Любой пользователь может зарегистрироваться на сайте
        """
        if self.action == 'create':
            self.permission_classes = [AllowAny]
        return super().get_permissions()


class PaymentListAPIView(ListAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    filter_backends = [filters.OrderingFilter]
    filterset_fields = ('well', 'lesson', 'payment_method')
    ordering_fields = ('date_payment',)

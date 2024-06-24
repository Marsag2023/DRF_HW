from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated, AllowAny
from users.models import User
from users.serializer import UserSerializer


class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

    def get_permissions(self):
        """
    Любой пользователь может зарегистрироваться на сайте
        """
        if self.action == 'create':
            self.permission_classes = [AllowAny]
        return super().get_permissions()

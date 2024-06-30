from django.urls import path
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.views import (TokenObtainPairView,
                                            TokenRefreshView)

from users.apps import UsersConfig
from users.views import (PaymentListAPIView, UserCreateAPIView,
                         UserDeleteAPIView, UserListAPIView,
                         UserRetrieveAPIView, UserUpdateAPIView)

app_name = UsersConfig.name


urlpatterns = [
    path("payments/", PaymentListAPIView.as_view(), name="payments_list"),
    path("register/", UserCreateAPIView.as_view(), name="register"),
    path("", UserListAPIView.as_view(), name="list"),
    path("retrieve/<int:pk>/", UserRetrieveAPIView.as_view(), name="retrieve"),
    path("update/<int:pk>/", UserUpdateAPIView.as_view(), name="update"),
    path("delete/<int:pk>/", UserDeleteAPIView.as_view(), name="delete"),
    path(
        "login/",
        TokenObtainPairView.as_view(permission_classes=(AllowAny,)),
        name="login",
    ),
    path(
        "token/refresh/",
        TokenRefreshView.as_view(permission_classes=(AllowAny,)),
        name="token_refresh",
    ),
]

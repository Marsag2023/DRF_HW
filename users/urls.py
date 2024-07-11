from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView
from users.apps import UsersConfig
from users.views import (PaymentListAPIView, UserCreateAPIView,
                         UserDeleteAPIView, UserListAPIView,
                         UserRetrieveAPIView, UserUpdateAPIView, PaymentCreateAPIView, UserTokenObtainPairView)

app_name = UsersConfig.name


urlpatterns = [
    path("register/", UserCreateAPIView.as_view(), name="register"),
    path("", UserListAPIView.as_view(), name="list"),
    path("retrieve/<int:pk>/", UserRetrieveAPIView.as_view(), name="retrieve"),
    path("update/<int:pk>/", UserUpdateAPIView.as_view(), name="update"),
    path("delete/<int:pk>/", UserDeleteAPIView.as_view(), name="delete"),
    path(
        "login/",
        UserTokenObtainPairView.as_view(), name="login"),
    path(
        "token/refresh/",
        TokenRefreshView.as_view(), name="token_refresh"),

    path('payments/', PaymentCreateAPIView.as_view(), name='payment-create'),
    path('payments/', PaymentListAPIView.as_view(), name='payment-list'),
]

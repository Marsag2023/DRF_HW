from rest_framework.serializers import ModelSerializer
from django.contrib.auth.hashers import make_password
from users.models import User, Payment
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

class PaymentSerializer(ModelSerializer):
    class Meta:
        model = Payment
        fields = '__all__'


class UserSerializer(ModelSerializer):

    class Meta:
        model = User
        fields = "__all__"

    extra_kwargs = {
        'password': {'write_only': True},
    }

    def create(self, validated_data):
        validated_data['password'] = make_password(validated_data['password'])
        return super(UserSerializer, self).create(validated_data)


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Добавление пользовательских полей в токен
        token['username'] = user.username
        token['email'] = user.email

        return token
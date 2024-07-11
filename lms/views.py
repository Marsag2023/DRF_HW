from rest_framework.generics import (CreateAPIView, DestroyAPIView,
                                     ListAPIView, RetrieveAPIView,
                                     UpdateAPIView, get_object_or_404)
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

from lms.models import Lesson, Subscription, Well
from lms.pagination import MyPagination
from lms.serializer import (LessonSerializer, SubscriptionSerializer,
                            WellDetailSerializer, WellSerializer)
from users.permissions import IsModerator, IsOwner
from lms.tasks import send_mail_update


class WellViewSet(ModelViewSet):
    queryset = Well.objects.all()
    serializer_class = WellSerializer
    pagination_class = MyPagination

    def get_permissions(self):
        if self.action == "create":
            self.permission_classes = (~IsModerator,)
        elif self.action in ["update", "retrieve"]:
            self.permission_classes = (IsModerator | IsOwner,)
        elif self.action == "destroy":
            self.permission_classes = (~IsModerator | IsOwner,)
        return super().get_permissions()

    def perform_create(self, serializer):
        well = serializer.save()
        well.owner = self.request.user
        well.save()

    def perform_update(self, serializer):
        well = serializer.save()
        send_mail_update.delay(well_id=well.pk)

    def get_serializer_class(self):

        if self.action == "retrieve":
            return WellDetailSerializer
        return WellSerializer


class LessonCreateAPIView(CreateAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    permission_classes = (~IsModerator,)

    def perform_create(self, serializer):
        lesson = serializer.save()
        lesson.owner = self.request.user
        lesson.save()


class LessonListAPIView(ListAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    pagination_class = MyPagination


class LessonRetrieveAPIView(RetrieveAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    permission_classes = (IsModerator | IsOwner,)


class LessonUpdateAPIView(UpdateAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    permission_classes = (IsModerator | IsOwner,)


class LessonDestroyAPIView(DestroyAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    permission_classes = (~IsModerator | IsOwner,)


class SubscriptionAPIView(APIView):
    serializer_class = SubscriptionSerializer

    def post(self, *args, **kwargs):
        owner = self.request.user
        well_id = self.request.data.get("well")
        well = get_object_or_404(Well, pk=well_id)
        sub_item = Subscription.objects.all().filter(owner=owner).filter(well=well)

        if sub_item.exists():
            sub_item.delete()
            message = "Подписка отключена"
        else:
            Subscription.objects.create(owner=owner, well=well)
            message = "Подписка включена"
        return Response({"Сообщние": message})

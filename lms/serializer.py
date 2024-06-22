from rest_framework.serializers import ModelSerializer

from lms.models import Well, Lesson


class WellSerializer(ModelSerializer):
    class Meta:
        model = Well
        fields = "__all__"


class LessonSerializer(ModelSerializer):
    class Meta:
        model = Lesson
        fields = "__all__"

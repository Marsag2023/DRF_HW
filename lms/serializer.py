from rest_framework.fields import SerializerMethodField
from rest_framework.serializers import ModelSerializer

from lms.models import Lesson, Well


class LessonSerializer(ModelSerializer):
    class Meta:
        model = Lesson
        fields = "__all__"


class WellSerializer(ModelSerializer):
    count_lessons = SerializerMethodField()

    def get_count_lessons(self, well):
        """
        Возвращает количество уроков в курсе
        """
        return Lesson.objects.filter(well=well).count()

    class Meta:
        model = Well
        fields = "__all__"


class WellDetailSerializer(ModelSerializer):
    well_lessons = SerializerMethodField()

    def get_well_lessons(self, well):
        lessons_set = Lesson.objects.filter(well=well)
        return [(lesson.title, lesson.description, lesson.url_video) for lesson in
                lessons_set]

    class Meta:
        model = Well
        fields = "__all__"

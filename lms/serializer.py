from rest_framework import serializers


from lms.models import Lesson, Subscription, Well
from lms.validators import UrlVideoValidator


class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = "__all__"
        validators = [UrlVideoValidator(field="url_video")]


class WellSerializer(serializers.ModelSerializer):
    count_lessons = serializers.SerializerMethodField()
    lessons = LessonSerializer(source="lesson_set", many=True, read_only=True)

    def get_count_lessons(self, well):
        """
        Возвращает количество уроков в курсе
        """
        return Lesson.objects.filter(well=well).count()

    class Meta:
        model = Well
        fields = "__all__"


class WellDetailSerializer(serializers.ModelSerializer):
    well_lessons = serializers.SerializerMethodField()
    subscription = serializers.SerializerMethodField()

    def get_well_lessons(self, well):
        lessons_set = Lesson.objects.filter(well=well)
        return [
            (lesson.title, lesson.description, lesson.url_video)
            for lesson in lessons_set
        ]

    def get_subscription(self, instance):
        owner = self.context["request"].user
        return (
            Subscription.objects.all()
            .filter(owner=owner)
            .filter(well=instance)
            .exists()
        )

    class Meta:
        model = Well
        fields = "__all__"


class SubscriptionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Subscription
        fields = "__all__"

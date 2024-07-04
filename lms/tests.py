import re

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from lms.models import Lesson, Subscription, Well
from users.models import User


class LessonTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create(email="test@sky.pro", password="12345")
        self.well = Well.objects.create(title="Тест", description="Тест")
        self.lesson = Lesson.objects.create(
            title="Тест",
            description="Тест",
            well=self.well,
            url_video="https://www.youtube.com/watch?v=8sv-6AN0_cg",
            owner=self.user,
        )
        self.client.force_authenticate(user=self.user)

    def test_lesson_retrieve(self):
        url = reverse("lms:lesson-retrieve", args=[self.lesson.pk])
        response = self.client.get(url)
        data = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data.get("title"), self.lesson.title)

    def test_create_lesson(self):
        """Тестирование создания урока"""
        url = reverse("lms:lesson-create")
        data = {
            "title": "Python",
            "description": "Язык программирования",
            "well": self.lesson.well.id,
            "url_video": "https://www.youtube.com/watch?v=8sv-6AN0_cg",
        }

        response = self.client.post(url, data=data)
        data = response.json()

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(data.get("title"), "Python")
        self.assertEqual(data.get("well"), self.lesson.well.id)
        self.assertEqual(data.get("description"), "Язык программирования")
        self.assertTrue(re.match(r"^https://www.youtube.com/", data.get("url_video")))
        self.assertEqual(Lesson.objects.all().count(), 2)

    def test_lesson_update(self):
        url = reverse("lms:lesson-update", args=[self.lesson.pk])
        data = {
            "title": "Тест2",
            "url_video": "https://www.youtube.com/watch",
        }
        response = self.client.patch(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data.get("title"), "Тест2")
        self.assertEqual(data.get("url_video"), "https://www.youtube.com/watch")

    def test_lesson_delete(self):
        url = reverse("lms:lesson-delete", args=[self.lesson.pk])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Lesson.objects.all().count(), 0)

    def test_lesson_list(self):
        url = reverse("lms:lesson-list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Lesson.objects.all().count(), 1)


class SubscriptionTestCase(APITestCase):

    def setUp(self):
        self.user = User.objects.create(email="test@sky.pro", password="12345")
        self.well = Well.objects.create(
            title="Тест", description="Тест", owner=self.user
        )
        self.client.force_authenticate(user=self.user)

    def test_subscription_create(self):
        self.url = reverse("lms:subscription")
        self.data = {"well": self.well.pk}
        response = self.client.post(self.url, self.data)
        data = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data, {"Сообщние": "Подписка включена"})

    def test_subscription_delete(self):
        self.url = reverse("lms:subscription")
        self.data = {"well": self.well.pk}
        Subscription.objects.create(well=self.well, owner=self.user)
        response = self.client.post(self.url, self.data)
        data = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data, {"Сообщние": "Подписка отключена"})
        self.assertEqual(
            Subscription.objects.filter(owner=self.user, well=self.well).count(), 0
        )
        self.assertEqual(Subscription.objects.filter(owner=self.user).count(), 0)
